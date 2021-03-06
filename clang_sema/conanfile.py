from conans import python_requires

common = python_requires('llvm-common/0.0.0@bincrafters/testing')

class ClangSema(common.LLVMModulePackage):
    version = common.LLVMModulePackage.version
    name = 'clang_sema'
    llvm_component = 'clang'
    llvm_module = 'Sema'
    llvm_requires = ['clang_headers', 'clang_ast', 'clang_analysis', 'clang_basic', 'clang_edit', 'clang_lex', 'llvm_support']
