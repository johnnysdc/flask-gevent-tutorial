import greenify

greenify.greenify()
assert greenify.patch_lib(
    "/usr/lib/oracle/19.5/client64/lib/libclntsh.so.19.1")

from app import app

