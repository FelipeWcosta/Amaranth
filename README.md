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
 
 If you want to migrate to Google Colab, you can install Amaranth HDL toolchain with:
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

 **To be continued...**
