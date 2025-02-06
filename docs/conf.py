# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# Project information
project = 'Roo Documentation'
copyright = '2024, Roo Project Team'
author = 'Roo Project Team'

# Extensions
extensions = [
    'myst_parser',
    'sphinxcontrib.mermaid',
]

# MyST configuration
myst_enable_extensions = [
    "colon_fence",
    "deflist",
]

# Mermaid configuration
mermaid_init_js = """
mermaid.initialize({
    startOnLoad:true,
    theme: 'neutral',
    securityLevel: 'strict',
});
"""

# Optional: Mermaid advanced parameters
# mermaid_params = ['-theme', 'neutral']

# HTML output settings
html_theme = 'justthedocs'
html_title = 'Roo Documentation'

# Additional configuration for Just the Docs theme
html_logo = None  # Add path to logo if you have one
html_favicon = None  # Add path to favicon if you have one

# Source file parsing
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# Exclude patterns
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# If you want to add more configuration options for Sphinx
# Add them here