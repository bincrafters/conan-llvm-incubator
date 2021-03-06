from conans import python_requires
import os

common = python_requires('llvm-common/0.0.0@bincrafters/testing')

class LLVMDebugInfoMSF(common.LLVMModulePackage):
    version = common.LLVMModulePackage.version
    name = 'llvm_debuginfo_msf'
    llvm_component = 'llvm'
    llvm_module = 'DebugInfoMSF'
    llvm_requires = ['llvm_headers', 'llvm_support', 'llvm_demangle']
