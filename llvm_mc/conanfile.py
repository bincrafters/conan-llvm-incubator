from conans import python_requires
import os

common = python_requires('llvm-common/0.0.0@bincrafters/testing')

class LLVMMC(common.LLVMModulePackage):
    version = common.LLVMModulePackage.version
    name = 'llvm_mc'
    llvm_component = 'llvm'
    llvm_module = 'MC'
    llvm_requires = ['llvm_headers', 'llvm_support']
