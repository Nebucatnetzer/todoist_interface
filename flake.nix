{
  description = "A Python API for various tools I use at work.";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.11";
    flake-utils.url = "github:numtide/flake-utils";
    poetry2nix.url = "github:nix-community/poetry2nix";
    poetry2nix.inputs.nixpkgs.follows = "nixpkgs";
  };
  outputs =
    { self, flake-utils, ... }@inputs:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = inputs.nixpkgs.legacyPackages.${system};
        poetry2nix = inputs.poetry2nix.lib.mkPoetry2Nix { inherit pkgs; };
        python = pkgs.python311.override {
          self = python;
          packageOverrides = final: prev: {
            wheel = prev.wheel.overridePythonAttrs (oA: rec {
              version = "0.45.1";
              src = oA.src.override (oA: {
                rev = "refs/tags/${version}";
                hash = "sha256-tgueGEWByS5owdA5rhXGn3qh1Vtf0HGYC6+BHfrnGAs=";
              });
            });
          };
        };
        pyEnv = poetry2nix.mkPoetryEnv {
          projectDir = ./.;
          editablePackageSources = {
            todoist_interface = ./todoist_interface;
          };
          overrides = poetry2nix.defaultPoetryOverrides.extend (
            self: super: {
              pyinstaller = super.pyinstaller.overridePythonAttrs (oldAttrs: {
                propagatedBuildInputs = oldAttrs.propagatedBuildInputs ++ [ pkgs.zlib ];
              });
              click = super.click.overridePythonAttrs (oldAttrs: {
                propagatedBuildInputs = oldAttrs.propagatedBuildInputs ++ [ super.flit-core ];
              });
            }
          );
          inherit python;
        };
        binary =
          {
            bintools-unwrapped,
            coreutils,
            glibc,
          }:
          pkgs.stdenv.mkDerivation {
            name = "todoist_interface";
            src = self;
            buildInputs = [
              coreutils
              glibc
              bintools-unwrapped
              pyEnv
            ];
            doCheck = true;
            checkPhase = ''
              python -m pytest tests
            '';
            buildPhase = ''
              pyinstaller -F todoist_interface/__main__.py -n todoist_interface --path=todoist_interface/
            '';
            installPhase = ''
              mkdir -p $out
              cp dist/todoist_interface "$out/todoist_interface"
            '';
          };
      in
      {
        devShells.default = pkgs.mkShell {
          shellHook = ''
            export PYTHONPATH="$PYTHONPATH":"$PWD"/todoist_interface
          '';
          buildInputs = [
            pyEnv
            pkgs.poetry
          ];
        };
        packages.binary = pkgs.callPackage binary { };
        packages.default = self.packages.${system}.binary;
      }
    );
}
