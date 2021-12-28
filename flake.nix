{
  description = "A Python API for various tools I use at work.";
  inputs = {
    nixpkgs.url = github:NixOS/nixpkgs/nixos-21.11;
    flake-utils.url = github:numtide/flake-utils;
    mach-nix.url = "github:DavHau/mach-nix";
  };

  outputs = { self, nixpkgs, flake-utils, mach-nix }:
    with flake-utils.lib; eachSystem allSystems (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        base-requirements = builtins.readFile ./requirements/base.txt;
        pyEnv = mach-nix.lib."${system}".mkPython {
          requirements = base-requirements + ''
            autopep8
            flake8
            pytest
            pytest-cov
            pyinstaller
          '';
        };
      in
      rec {
        devShell."${system}" = pkgs.mkShell {
          buildInputs = [ pyEnv ];
        };
        packages =
          let
            binary = { autoPatchelfHook, ... }: pkgs.stdenv.mkDerivation rec {
              name = "todoist_interface";
              src = self;
              nativeBuildInputs = [
                autoPatchelfHook
              ];
              buildInputs = [
                pkgs.coreutils
                pkgs.glibc
                pkgs.bintools-unwrapped
                pyEnv
              ];
              phases = [ "unpackPhase" "buildPhase" "installPhase" ];
              buildPhase = ''
                export PATH="${pkgs.lib.makeBinPath buildInputs}";
                python -m pytest tests
                pyinstaller -F todoist_interface/__main__.py -n todoist_interface
              '';
              installPhase = ''
                mkdir -p $out
                cp /build/source/dist/todoist_interface "$out/todoist_interface"
              '';
            };
          in
          pkgs.callPackage binary { };

        defaultPackage = packages;
      });
}
