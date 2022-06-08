"""
My first lev tool
Homepage: -
GitHub: -
Type: IMAGE-BASED
Version: v1.0.0
"""
import levrt
from levrt import Cr, ctx, remote, annot
from levrt.annot.cats import Attck, BlackArch

@annot.meta(
    desc="Hello",
    params=[annot.Param("name", "person name")],
    cats=[Attck.Reconnaissance],
)
def hello(name: str = "world") -> Cr:
    """
    Unique tool mode for Hello World
    ```
    await hello("world")
    ```
    """
    @levrt.remote
    def entry():
        ctx.set(msg=f"Hello, {name}!")

    return Cr("alpine:latest", entry=entry())


@annot.meta(
    desc="Hi",
    params=[annot.Param("name", "person name")],
    cats=[Attck.Reconnaissance],
)
def hi(name: str = "world") -> Cr:
    """
    Second tool mode of Hello World
    ```
    await hi("world")
    ```
    """
    @levrt.remote
    def entry():
        ctx.set(msg=f"Hi, {name}!")

    return Cr("alpine:latest", entry=entry())


@annot.meta(
    desc="Exp",
    params=[annot.Param("name", "person name")],
    cats=[Attck.Reconnaissance],
)
def exp(length: int = 9) -> Cr:
    """
    The third tool mode of Hello World
    ```
    await exp(9)
    ```
    """

    @levrt.remote
    def entry():
        import sys
        sys.path.append('/usr/local/lib/python3.10/site-packages')
        import numpy
        res = round(numpy.e, length)
        ctx.set(msg=res)

    return Cr("5410f01fd9cf", entry=entry())


__lev__ = annot.meta([hello, hi],
                     desc = "hello world", # name of tool
                     cats = {
                        Attck: [Attck.Reconnaissance] # ATT&CK
                     })
