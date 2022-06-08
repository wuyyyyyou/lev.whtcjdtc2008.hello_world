import levrt
from lev.whtcjdtc2009.hello_world import hello

async def main():
    doc = await hello.exp(9)
    data = await doc.get()
    print(data["msg"])


if __name__ == "__main__":
    levrt.run(main())
