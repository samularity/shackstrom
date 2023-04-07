{ pkgs ? import <nixpkgs> {} }:
pkgs.writers.writePython3 "test_python3" {
  libraries = [ pkgs.python3Packages.requests pkgs.python3Packages.paho-mqtt  ];
} 
(builtins.readFile ./shackstrom.py)