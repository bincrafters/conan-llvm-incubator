from conans import python_requires

common = python_requires('llvm-common/0.0.0@bincrafters/testing')

class ClangAST(common.LLVMModulePackage):
    version = common.LLVMModulePackage.version
    name = 'clang_ast'
    llvm_component = 'clang'
    llvm_module = 'AST'
    llvm_requires = ['clang_headers', 'clang_basic', 'clang_lex']
