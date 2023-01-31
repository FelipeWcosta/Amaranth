# Amaranth
 Repository with Amaranth HDL toolchain tutorials
## Resolving the dependencies
 Using the Visual Studio Code editor, Amaranth HDL toolchain can be installed using the following 
 command line using PyPI:
 ```
    py -m pip install amaranth
 ```
 Pay attention and check if your Python version is compatible. You can find more details [here][def].

 [def]: https://amaranth-lang.org/docs/amaranth/latest/install.html
 
 For working with *domains* Visual Studio Code is not working well locally. So we migrated to Google Colab, you can install Amaranth HDL toolchain with:
 ```
   !pip install amaranth
 ```
 ## Creating a `module`
  In the Google Colab script, you must install Amaranth in order to create a new `module` as follows:
  ```
   !pip install amaranth
  ```
  ```
   from amaranth import Elaboratable, Module
   from amaranth.build import Platform


   class ThingBlock(Elaboratable):
       def __init__(self):
           pass

       def elaborate(self, platform: Platform) -> Module:
           m = Module()
           return m
  ```
  ```
  from amaranth import ClockDomain, Module
  from amaranth.cli import main
  import sys


  sys.argv=['']
  del sys


  if __name__ == "__main__":
      sync = ClockDomain()

      block = ThingBlock()

      m = Module()
      m.domains += sync
      m.submodules += block

      main(m, ports=[sync.clk, sync.rst])
  ```

 **To be continued...**
