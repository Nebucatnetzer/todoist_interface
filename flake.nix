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
          requirements = base-requirements;
        };
      in
      rec {
        devShell = mach-nix.lib."${system}".mkPythonShell {
          requirements = base-requirements + ''
            flake8
            autopep8
            pytest
            pytest-cov
            pyinstaller
          '';
        };
      });
}
