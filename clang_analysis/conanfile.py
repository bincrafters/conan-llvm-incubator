from conans import python_requires

common = python_requires('llvm-common/0.0.0@bincrafters/testing')

class ClangAnalysis(common.LLVMModulePackage):
    version = common.LLVMModulePackage.version
    name = 'clang_analysis'
    llvm_component = 'clang'
    llvm_module = 'Analysis'
    llvm_requires = ['clang_headers', 'clang_ast', 'clang_basic', 'clang_lex', 'llvm_support']
