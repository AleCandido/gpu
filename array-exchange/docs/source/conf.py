# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


import pathlib

here = pathlib.Path(__file__).absolute().parent

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "interoperability"
copyright = "2022, Alessandro Candido"
author = "Alessandro Candido"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]

# https://github.com/readthedocs/readthedocs.org/issues/1139#issuecomment-312626491
def run_apidoc(_):
    import sys  # pylint: disable=import-outside-toplevel

    from sphinx.ext.apidoc import main  # pylint: disable=import-outside-toplevel

    sys.path.append(str(here.parent))
    for pkg, docs_dest in dict(benchmark=here / "benchmark").items():
        package = here.parents[1] / "src" / pkg
        main(["--module-first", "-o", str(docs_dest), str(package)])
        (docs_dest / "modules.rst").unlink()


def setup(app):
    """Configure Sphinx"""
    app.setup_extension("sphinx.ext.autodoc")
    app.connect("builder-inited", run_apidoc)
