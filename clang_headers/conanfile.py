from conans import python_requires

common = python_requires('llvm-common/0.0.0@bincrafters/testing')

class ClangHeaders(common.LLVMModulePackage):
    version = common.LLVMModulePackage.version
    name = 'clang_headers'
    llvm_component = 'clang'
    header_only = True
    include_dirs = ['']
