from conans import python_requires

common = python_requires('llvm-common/0.0.0@bincrafters/testing')

class ClangIndex(common.LLVMModulePackage):
    version = common.LLVMModulePackage.version
    name = 'clang_index'
    llvm_component = 'clang'
    llvm_module = 'Index'
    llvm_requires = ['clang_headers', 'clang_ast', 'clang_basic', 'clang_format', 'clang_frontend', 'clang_rewrite', 'clang_serialization', 'clang_tooling_core', 'llvm_core', 'llvm_support']
