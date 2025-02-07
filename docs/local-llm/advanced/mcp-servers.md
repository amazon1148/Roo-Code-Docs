# MCP Server List

This document provides a comprehensive list of Model Context Protocol (MCP) servers for software development lifecycle integration. Each server includes installation methods and tool definitions where available.

## Confirmed Packages & Repositories

### Development Tools
* [OpenAPI Client Generator](https://github.com/orhanveli/openapi-client-generator-mcp)
  * Run: `npx @orhanveli/openapi-client-generator-mcp`
  * Description: Generate TypeScript API clients from OpenAPI specs
  * Tool Definitions:
    ```

### Build & CI/CD Tools

* [Make MCP](https://github.com/wrale-makefile-make)
  * Run: `npx @wrale/makefile-mcp`
  * Description: Build automation and Makefile management
  * Tool Definitions:
    ```json
    {
      "name": "make_automation",
      "description": "Build automation and Makefile management",
      "tools": [
        {
          "name": "run_target",
          "description": "Execute Makefile target",
          "parameters": {
            "type": "object",
            "properties": {
              "target": {"type": "string", "description": "Target to execute"},
              "makefile": {"type": "string", "description": "Path to Makefile"},
              "variables": {
                "type": "object",
                "additionalProperties": {"type": "string"},
                "description": "Make variables to set"
              },
              "directory": {"type": "string", "description": "Working directory"}
            },
            "required": ["target"]
          }
        },
        {
          "name": "list_targets",
          "description": "List available Makefile targets",
          "parameters": {
            "type": "object",
            "properties": {
              "makefile": {"type": "string", "description": "Path to Makefile"}
            }
          }
        }
      ]
    }
    ```

* [GitHub Pera](https://github.com/kazuph/github-pera1)
  * Run: `npx @kazuph/github-pera-mcp`
  * Description: GitHub workflow and CI/CD automation
  * Tool Definitions:
    ```json
    {
      "name": "github_automation",
      "description": "GitHub workflow and CI/CD automation",
      "tools": [
        {
          "name": "create_workflow",
          "description": "Create GitHub Actions workflow",
          "parameters": {
            "type": "object",
            "properties": {
              "name": {"type": "string", "description": "Workflow name"},
              "trigger": {
                "type": "object",
                "properties": {
                  "event": {"type": "string"},
                  "branches": {"type": "array", "items": {"type": "string"}}
                }
              },
              "jobs": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "name": {"type": "string"},
                    "steps": {"type": "array", "items": {"type": "string"}}
                  }
                }
              }
            },
            "required": ["name", "trigger", "jobs"]
          }
        },
        {
          "name": "trigger_workflow",
          "description": "Trigger GitHub Actions workflow",
          "parameters": {
            "type": "object",
            "properties": {
              "workflow": {"type": "string", "description": "Workflow file name"},
              "ref": {"type": "string", "description": "Git reference"}
            },
            "required": ["workflow"]
          }
        }
      ]
    }
    ```json
    {
      "name": "openapi_client_generator",
      "description": "Generate TypeScript API clients from OpenAPI specs",
      "tools": [{
        "name": "generate_client",
        "description": "Generate a TypeScript client from OpenAPI specification",
        "parameters": {
          "type": "object",
          "properties": {
            "spec_path": {"type": "string", "description": "Path to OpenAPI spec file"},
            "output_dir": {"type": "string", "description": "Output directory"},
            "client_name": {"type": "string", "description": "Name for generated client"}
          },
          "required": ["spec_path"]
        }
      }]
    }
    ```

* [Azure OpenAI Web Browser](https://github.com/kimtth/mcp-aoai-web-browsing)
  * Run: `npx @kimtth/mcp-aoai-web-browsing`
  * Description: Browser automation with Azure OpenAI integration
  * Tool Definitions:
    ```json
    {
      "name": "azure_openai_browser",
      "description": "Browser automation with Azure OpenAI integration",
      "tools": [
        {
          "name": "browse_url",
          "description": "Navigate to URL and extract content",
          "parameters": {
            "type": "object",
            "properties": {
              "url": {"type": "string", "description": "URL to navigate to"},
              "selector": {"type": "string", "description": "Optional CSS selector to extract"}
            },
            "required": ["url"]
          }
        },
        {
          "name": "screenshot",
          "description": "Take screenshot of webpage",
          "parameters": {
            "type": "object",
            "properties": {
              "output_path": {"type": "string", "description": "Path to save screenshot"},
              "full_page": {"type": "boolean", "description": "Capture full page"}
            },
            "required": ["output_path"]
          }
        }
      ]
    }
    ```

### Development Environment Tools

* [Docker MCP](https://github.com/QuantGeekDev/docker-mcp)
  * Run: `npx @quantgeekdev/docker-mcp`
  * Description: Docker container management and orchestration
  * Tool Definitions:
    ```json
    {
      "name": "docker_management",
      "description": "Docker container and image management",
      "tools": [
        {
          "name": "run_container",
          "description": "Run a Docker container",
          "parameters": {
            "type": "object",
            "properties": {
              "image": {"type": "string", "description": "Docker image name"},
              "tag": {"type": "string", "description": "Image tag"},
              "ports": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Port mappings (host:container)"
              },
              "env": {
                "type": "object",
                "additionalProperties": {"type": "string"},
                "description": "Environment variables"
              }
            },
            "required": ["image"]
          }
        },
        {
          "name": "build_image",
          "description": "Build Docker image from Dockerfile",
          "parameters": {
            "type": "object",
            "properties": {
              "path": {"type": "string", "description": "Path to Dockerfile directory"},
              "tag": {"type": "string", "description": "Image tag"},
              "buildArgs": {
                "type": "object",
                "additionalProperties": {"type": "string"},
                "description": "Build arguments"
              }
            },
            "required": ["path", "tag"]
          }
        },
        {
          "name": "manage_container",
          "description": "Manage container lifecycle",
          "parameters": {
            "type": "object",
            "properties": {
              "containerId": {"type": "string", "description": "Container ID or name"},
              "action": {
                "type": "string",
                "enum": ["start", "stop", "restart", "remove"],
                "description": "Action to perform"
              }
            },
            "required": ["containerId", "action"]
          }
        }
      ]
    }
    ```

* [Keycloak](https://github.com/ChristophEnglisch/keycloak-model-context-protocol)
  * Run: `npx @christophenglisch/keycloak-mcp`
  * Description: Keycloak user management and authentication
  * Tool Definitions:
    ```json
    {
      "name": "keycloak_management",
      "description": "Keycloak user and authentication management",
      "tools": [
        {
          "name": "create_user",
          "description": "Create new user in Keycloak",
          "parameters": {
            "type": "object",
            "properties": {
              "username": {"type": "string", "description": "Username"},
              "email": {"type": "string", "description": "Email address"},
              "firstName": {"type": "string", "description": "First name"},
              "lastName": {"type": "string", "description": "Last name"},
              "enabled": {"type": "boolean", "description": "Account enabled status"},
              "roles": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Roles to assign"
              }
            },
            "required": ["username", "email"]
          }
        },
        {
          "name": "get_user",
          "description": "Get user details",
          "parameters": {
            "type": "object",
            "properties": {
              "userId": {"type": "string", "description": "User ID"},
              "username": {"type": "string", "description": "Username"}
            },
            "oneOf": ["userId", "username"]
          }
        },
        {
          "name": "update_user",
          "description": "Update user details",
          "parameters": {
            "type": "object",
            "properties": {
              "userId": {"type": "string", "description": "User ID"},
              "attributes": {
                "type": "object",
                "additionalProperties": true,
                "description": "User attributes to update"
              }
            },
            "required": ["userId", "attributes"]
          }
        },
        {
          "name": "delete_user",
          "description": "Delete user",
          "parameters": {
            "type": "object",
            "properties": {
              "userId": {"type": "string", "description": "User ID"}
            },
            "required": ["userId"]
          }
        }
      ]
    }
    ```

* [Python REPL](https://github.com/what-the-func/mcp-python)
  * Run: `uvx mcp-python`
  * Description: Interactive Python code execution and environment
  * Tool Definitions:
    ```json
    {
      "name": "python_repl",
      "description": "Python code execution and environment management",
      "tools": [
        {
          "name": "execute_code",
          "description": "Execute Python code in isolated environment",
          "parameters": {
            "type": "object",
            "properties": {
              "code": {"type": "string", "description": "Python code to execute"},
              "timeout": {"type": "integer", "description": "Execution timeout in seconds"},
              "environment": {
                "type": "object",
                "properties": {
                  "pythonPath": {"type": "string"},
                  "dependencies": {
                    "type": "array",
                    "items": {"type": "string"}
                  }
                }
              }
            },
            "required": ["code"]
          }
        },
        {
          "name": "install_package",
          "description": "Install Python package in environment",
          "parameters": {
            "type": "object",
            "properties": {
              "package": {"type": "string", "description": "Package name and version"},
              "index_url": {"type": "string", "description": "Package index URL"}
            },
            "required": ["package"]
          }
        }
      ]
    }
    ```

### Testing & Quality Tools

* [Playwright MCP](https://github.com/automata-labs/playwright)
  * Run: `npx @automata-labs/playwright-mcp`
  * Description: Browser automation and testing
  * Tool Definitions:
    ```json
    {
      "name": "playwright_automation",
      "description": "Browser automation and testing with Playwright",
      "tools": [
        {
          "name": "run_test",
          "description": "Run browser test script",
          "parameters": {
            "type": "object",
            "properties": {
              "script": {"type": "string", "description": "Test script content"},
              "browser": {
                "type": "string",
                "enum": ["chromium", "firefox", "webkit"],
                "description": "Browser to use"
              },
              "screenshot": {
                "type": "object",
                "properties": {
                  "enabled": {"type": "boolean"},
                  "path": {"type": "string"}
                }
              }
            },
            "required": ["script"]
          }
        },
        {
          "name": "record_test",
          "description": "Record browser interactions as test",
          "parameters": {
            "type": "object",
            "properties": {
              "url": {"type": "string", "description": "Starting URL"},
              "outputPath": {"type": "string", "description": "Path to save recorded test"}
            },
            "required": ["url", "outputPath"]
          }
        }
      ]
    }
    ```

* [Crypto Price](https://github.com/truss44/mcp-crypto-price)
  * Crypto analysis via CoinCap API
  * Install: `npm install @truss44/mcp-crypto-price`

### Shell & Terminal Tools

* [Shell Server](https://github.com/tumf/mcp-shell-server)
  * Run: `npx @tumf/shell-mcp`
  * Description: Advanced shell operations and scripting
  * Tool Definitions:
    ```json
    {
      "name": "shell_operations",
      "description": "Advanced shell operations and scripting",
      "tools": [
        {
          "name": "execute_script",
          "description": "Execute shell script with advanced options",
          "parameters": {
            "type": "object",
            "properties": {
              "script": {"type": "string", "description": "Script content"},
              "interpreter": {
                "type": "string",
                "enum": ["bash", "zsh", "sh", "fish"],
                "description": "Shell interpreter to use"
              },
              "environment": {
                "type": "object",
                "additionalProperties": {"type": "string"},
                "description": "Environment variables"
              },
              "workingDir": {"type": "string", "description": "Working directory"}
            },
            "required": ["script"]
          }
        },
        {
          "name": "manage_processes",
          "description": "Manage background processes",
          "parameters": {
            "type": "object",
            "properties": {
              "operation": {
                "type": "string",
                "enum": ["start", "stop", "list", "kill"],
                "description": "Process operation"
              },
              "processId": {"type": "string", "description": "Process ID for operations"},
              "signal": {
                "type": "string",
                "enum": ["SIGTERM", "SIGKILL", "SIGINT"],
                "description": "Signal to send"
              }
            },
            "required": ["operation"]
          }
        }
      ]
    }
    ```

* [HD Research Shell](https://github.com/hdresearch/shell)
  * Run: `npx @hdresearch/shell-mcp`
  * Description: Research-focused shell environment
  * Tool Definitions:
    ```json
    {
      "name": "research_shell",
      "description": "Research-oriented shell environment",
      "tools": [
        {
          "name": "execute_pipeline",
          "description": "Execute research data pipeline",
          "parameters": {
            "type": "object",
            "properties": {
              "steps": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "command": {"type": "string"},
                    "timeout": {"type": "integer"},
                    "dependencies": {"type": "array", "items": {"type": "string"}}
                  }
                },
                "description": "Pipeline steps"
              },
              "environment": {"type": "object", "additionalProperties": {"type": "string"}},
              "logLevel": {
                "type": "string",
                "enum": ["debug", "info", "warning", "error"],
                "description": "Logging detail level"
              }
            },
            "required": ["steps"]
          }
        },
        {
          "name": "manage_workspace",
          "description": "Manage research workspace",
          "parameters": {
            "type": "object",
            "properties": {
              "operation": {
                "type": "string",
                "enum": ["create", "snapshot", "restore", "clean"],
                "description": "Workspace operation"
              },
              "name": {"type": "string", "description": "Workspace name"},
              "template": {"type": "string", "description": "Workspace template"}
            },
            "required": ["operation", "name"]
          }
        }
      ]
    }
    ```

* [Odysseus Shell](https://github.com/odysseus0/shell)
  * Run: `npx @odysseus0/shell-mcp`
  * Description: Enhanced shell with advanced scripting capabilities
  * Tool Definitions:
    ```json
    {
      "name": "odysseus_shell",
      "description": "Enhanced shell with advanced scripting",
      "tools": [
        {
          "name": "execute_advanced_script",
          "description": "Execute script with advanced control flow",
          "parameters": {
            "type": "object",
            "properties": {
              "script": {"type": "string", "description": "Script content"},
              "flowControl": {
                "type": "object",
                "properties": {
                  "errorHandling": {"type": "string", "enum": ["continue", "abort", "retry"]},
                  "maxRetries": {"type": "integer"},
                  "timeout": {"type": "integer"}
                }
              },
              "variables": {
                "type": "object",
                "additionalProperties": {"type": "string"},
                "description": "Script variables"
              }
            },
            "required": ["script"]
          }
        },
        {
          "name": "create_automation",
          "description": "Create shell automation task",
          "parameters": {
            "type": "object",
            "properties": {
              "name": {"type": "string", "description": "Automation name"},
              "trigger": {
                "type": "object",
                "properties": {
                  "type": {"type": "string", "enum": ["schedule", "file", "process"]},
                  "condition": {"type": "string"}
                }
              },
              "actions": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "command": {"type": "string"},
                    "onSuccess": {"type": "string"},
                    "onFailure": {"type": "string"}
                  }
                }
              }
            },
            "required": ["name", "actions"]
          }
        }
      ]
    }
    ```

* [iTerm MCP](https://github.com/ferrislucas/iterm)
  * Run: `npx @ferrislucas/iterm-mcp`
  * Description: Terminal emulator integration for development
  * Tool Definitions:
    ```json
    {
      "name": "iterm_integration",
      "description": "iTerm terminal emulator integration",
      "tools": [
        {
          "name": "create_tab",
          "description": "Create new iTerm tab",
          "parameters": {
            "type": "object",
            "properties": {
              "command": {"type": "string", "description": "Initial command to run"},
              "profile": {"type": "string", "description": "iTerm profile name"},
              "directory": {"type": "string", "description": "Working directory"}
            }
          }
        },
        {
          "name": "run_command",
          "description": "Run command in current or specified tab",
          "parameters": {
            "type": "object",
            "properties": {
              "command": {"type": "string", "description": "Command to execute"},
              "tab_id": {"type": "string", "description": "Target tab ID (optional)"},
              "wait_for_exit": {"type": "boolean", "description": "Wait for command completion"}
            },
            "required": ["command"]
          }
        },
        {
          "name": "split_pane",
          "description": "Split current pane",
          "parameters": {
            "type": "object",
            "properties": {
              "direction": {
                "type": "string",
                "enum": ["horizontal", "vertical"],
                "description": "Split direction"
              },
              "command": {"type": "string", "description": "Initial command for new pane"},
              "profile": {"type": "string", "description": "iTerm profile name"}
            },
            "required": ["direction"]
          }
        }
      ]
    }
    ```

* [CLI MCP](https://github.com/mladensu/cli-mcp-server)
  * Run: `npx @mladensu/cli-mcp`
  * Description: Command-line interface and shell integration
  * Tool Definitions:
    ```json
    {
      "name": "cli_shell",
      "description": "Command-line and shell operations",
      "tools": [
        {
          "name": "execute_command",
          "description": "Execute shell command",
          "parameters": {
            "type": "object",
            "properties": {
              "command": {"type": "string", "description": "Command to execute"},
              "cwd": {"type": "string", "description": "Working directory"},
              "env": {
                "type": "object",
                "additionalProperties": {"type": "string"},
                "description": "Environment variables"
              },
              "timeout": {"type": "integer", "description": "Execution timeout in ms"}
            },
            "required": ["command"]
          }
        },
        {
          "name": "pipe_commands",
          "description": "Execute piped shell commands",
          "parameters": {
            "type": "object",
            "properties": {
              "commands": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Commands to pipe together"
              },
              "cwd": {"type": "string"},
              "shell": {"type": "string", "description": "Shell to use (bash/zsh/etc)"}
            },
            "required": ["commands"]
          }
        },
        {
          "name": "stream_output",
          "description": "Execute command with streamed output",
          "parameters": {
            "type": "object",
            "properties": {
              "command": {"type": "string"},
              "filter": {"type": "string", "description": "Output filter regex"},
              "maxLines": {"type": "integer"}
            },
            "required": ["command"]
          }
        }
      ]
    }
    ```

* [Windows CLI MCP](https://github.com/simonb97/windows-cli-mcp-server)
  * Run: `npx @simonb97/windows-cli-mcp`
  * Description: Windows-specific CLI and PowerShell integration
  * Tool Definitions:
    ```json
    {
      "name": "windows_cli",
      "description": "Windows command-line operations",
      "tools": [
        {
          "name": "powershell_command",
          "description": "Execute PowerShell command",
          "parameters": {
            "type": "object",
            "properties": {
              "command": {"type": "string", "description": "PowerShell command"},
              "executionPolicy": {
                "type": "string",
                "enum": ["Restricted", "AllSigned", "RemoteSigned", "Unrestricted"],
                "description": "PowerShell execution policy"
              },
              "elevated": {"type": "boolean", "description": "Run with elevated privileges"}
            },
            "required": ["command"]
          }
        },
        {
          "name": "cmd_command",
          "description": "Execute CMD command",
          "parameters": {
            "type": "object",
            "properties": {
              "command": {"type": "string", "description": "CMD command"},
              "codePage": {"type": "string", "description": "Command prompt code page"},
              "waitOnExit": {"type": "boolean", "description": "Wait for command completion"}
            },
            "required": ["command"]
          }
        }
      ]
    }
    ```(https://github.com/seanivore/mcp-code-analyzer)
  * Python code analysis and debugging
  * Install: `pip install mcp-code-analyzer`

* [PyPI Query](https://github.com/loonghao/pypi-query-mcp-server)
  * Query PyPI packages and dependencies
  * Install: `pip install pypi-query-mcp-server`

* [Photoshop Python API](https://github.com/loonghao/photoshop-python-api-mcp-server)
  * Control Photoshop via Python API
  * Install: `pip install photoshop-python-api-mcp-server`

### Package Management Tools

* [Package Version Checker](https://github.com/sammcj/package-version)
  * Run: `npx @sammcj/package-version-mcp`
  * Description: Package version management and analysis
  * Tool Definitions:
    ```json
    {
      "name": "package_version_checker",
      "description": "Package version management and analysis",
      "tools": [
        {
          "name": "check_versions",
          "description": "Check package versions and updates",
          "parameters": {
            "type": "object",
            "properties": {
              "packages": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Package names to check"
              },
              "registry": {"type": "string", "description": "Package registry URL"},
              "updateLevel": {
                "type": "string",
                "enum": ["patch", "minor", "major"],
                "description": "Maximum update level to consider"
              }
            },
            "required": ["packages"]
          }
        },
        {
          "name": "analyze_dependencies",
          "description": "Analyze project dependencies",
          "parameters": {
            "type": "object",
            "properties": {
              "path": {"type": "string", "description": "Path to project"},
              "type": {
                "type": "string",
                "enum": ["npm", "yarn", "pnpm"],
                "description": "Package manager type"
              },
              "includeDevDependencies": {"type": "boolean"}
            },
            "required": ["path"]
          }
        }
      ]
    }
    ```

* [Package Documentation Viewer](https://github.com/sammcj/package-docs)
  * Run: `npx @sammcj/package-docs-mcp`
  * Description: View and search package documentation
  * Tool Definitions:
    ```json
    {
      "name": "package_docs",
      "description": "Package documentation access and search",
      "tools": [
        {
          "name": "search_docs",
          "description": "Search package documentation",
          "parameters": {
            "type": "object",
            "properties": {
              "package": {"type": "string", "description": "Package name"},
              "version": {"type": "string", "description": "Package version"},
              "query": {"type": "string", "description": "Search query"},
              "section": {
                "type": "string",
                "enum": ["api", "guide", "examples", "all"],
                "description": "Documentation section to search"
              }
            },
            "required": ["package", "query"]
          }
        },
        {
          "name": "get_api_docs",
          "description": "Get API documentation",
          "parameters": {
            "type": "object",
            "properties": {
              "package": {"type": "string", "description": "Package name"},
              "version": {"type": "string", "description": "Package version"},
              "method": {"type": "string", "description": "Specific API method"}
            },
            "required": ["package"]
          }
        }
      ]
    }
    ```
* [TxtAI Assistant](https://github.com/rmtech1/txtai-assistant-mcp)
  * Semantic search and memory management
  * Install: `pip install txtai-assistant-mcp`

* [Zotero Integration](https://github.com/kujenga/zotero-mcp)
  * Interact with Zotero reference manager
  * Install: `pip install zotero-mcp`

* [Notes Manager](https://github.com/truaxki/mcp-notes)
  * Persistent note management system
  * Install: `pip install mcp-notes`

### Code Management Tools

* [Codex Keeper](https://github.com/aindreyway/codex-keeper)
  * Run: `npx @aindreyway/codex-keeper-mcp`
  * Description: Code snippet and knowledge management
  * Tool Definitions:
    ```json
    {
      "name": "codex_keeper",
      "description": "Code snippet and knowledge management",
      "tools": [
        {
          "name": "save_snippet",
          "description": "Save code snippet with metadata",
          "parameters": {
            "type": "object",
            "properties": {
              "code": {"type": "string", "description": "Code snippet content"},
              "language": {"type": "string", "description": "Programming language"},
              "tags": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Categorization tags"
              },
              "description": {"type": "string", "description": "Snippet description"},
              "visibility": {
                "type": "string",
                "enum": ["private", "team", "public"],
                "description": "Snippet visibility"
              }
            },
            "required": ["code", "language"]
          }
        },
        {
          "name": "search_snippets",
          "description": "Search code snippets",
          "parameters": {
            "type": "object",
            "properties": {
              "query": {"type": "string", "description": "Search query"},
              "language": {"type": "string", "description": "Filter by language"},
              "tags": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Filter by tags"
              }
            },
            "required": ["query"]
          }
        }
      ]
    }
    ```

### Database Tools

* [MongoDB MCP](https://github.com/kiliczsh/mcp-mongo-server)
  * Run: `npx @kiliczsh/mcp-mongo-server`
  * Description: MongoDB database operations and management
  * Tool Definitions:
    ```json
    {
      "name": "mongodb_operations",
      "description": "MongoDB database operations and management",
      "tools": [
        {
          "name": "execute_query",
          "description": "Execute MongoDB query",
          "parameters": {
            "type": "object",
            "properties": {
              "database": {"type": "string", "description": "Database name"},
              "collection": {"type": "string", "description": "Collection name"},
              "operation": {
                "type": "string",
                "enum": ["find", "aggregate", "count", "distinct"],
                "description": "Query operation type"
              },
              "query": {
                "type": "object",
                "description": "Query parameters"
              },
              "options": {
                "type": "object",
                "properties": {
                  "limit": {"type": "integer"},
                  "skip": {"type": "integer"},
                  "sort": {"type": "object"}
                }
              }
            },
            "required": ["database", "collection", "operation", "query"]
          }
        },
        {
          "name": "manage_indexes",
          "description": "Manage MongoDB indexes",
          "parameters": {
            "type": "object",
            "properties": {
              "database": {"type": "string"},
              "collection": {"type": "string"},
              "operation": {
                "type": "string",
                "enum": ["create", "drop", "list"],
                "description": "Index operation"
              },
              "index": {
                "type": "object",
                "description": "Index specification"
              },
              "options": {
                "type": "object",
                "properties": {
                  "unique": {"type": "boolean"},
                  "sparse": {"type": "boolean"},
                  "background": {"type": "boolean"}
                }
              }
            },
            "required": ["database", "collection", "operation"]
          }
        }
      ]
    }
    ```

* [SQLite MCP](https://github.com/johnnyoshika/sqlite-npx)
  * Run: `npx @johnnyoshika/sqlite-mcp`
  * Description: SQLite database management and queries
  * Tool Definitions:
    ```json
    {
      "name": "sqlite_operations",
      "description": "SQLite database operations",
      "tools": [
        {
          "name": "execute_query",
          "description": "Execute SQLite query",
          "parameters": {
            "type": "object",
            "properties": {
              "database": {"type": "string", "description": "Database file path"},
              "query": {"type": "string", "description": "SQL query"},
              "params": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Query parameters"
              },
              "options": {
                "type": "object",
                "properties": {
                  "readonly": {"type": "boolean"},
                  "timeout": {"type": "integer"}
                }
              }
            },
            "required": ["database", "query"]
          }
        },
        {
          "name": "analyze_schema",
          "description": "Analyze database schema",
          "parameters": {
            "type": "object",
            "properties": {
              "database": {"type": "string", "description": "Database file path"},
              "table": {"type": "string", "description": "Specific table to analyze"}
            },
            "required": ["database"]
          }
        }
      ]
    }
    ```
* [SQLite Explorer](https://github.com/hannesrudolph/sqlite-explorer-fastmcp-mcp-server)
  * Safe, read-only SQLite database access
  * Install: `pip install sqlite-explorer-fastmcp`

* [Stock Trader](https://github.com/wshobson/mcp-trader)
  * Stock trading and market analysis
  * Install: `pip install mcp-trader`

* [Logic Calculator](https://github.com/angrysky56/mcp-logic)
  * AI-powered logic calculations using Prover9/Mace4
  * Install: `pip install mcp-logic`

### Infrastructure & Cloud Tools

* [Kubernetes MCP](https://github.com/strowk/kubernetes)
  * Run: `npx @strowk/kubernetes-mcp`
  * Description: Kubernetes cluster management and operations
  * Tool Definitions:
    ```json
    {
      "name": "kubernetes_operations",
      "description": "Kubernetes cluster management",
      "tools": [
        {
          "name": "manage_resources",
          "description": "Manage Kubernetes resources",
          "parameters": {
            "type": "object",
            "properties": {
              "operation": {
                "type": "string",
                "enum": ["apply", "delete", "get", "describe"],
                "description": "Resource operation"
              },
              "resource": {
                "type": "object",
                "properties": {
                  "kind": {"type": "string"},
                  "name": {"type": "string"},
                  "namespace": {"type": "string"},
                  "manifest": {"type": "object"}
                },
                "required": ["kind"]
              },
              "options": {
                "type": "object",
                "properties": {
                  "wait": {"type": "boolean"},
                  "timeout": {"type": "integer"}
                }
              }
            },
            "required": ["operation", "resource"]
          }
        },
        {
          "name": "monitor_resources",
          "description": "Monitor Kubernetes resources",
          "parameters": {
            "type": "object",
            "properties": {
              "resources": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "kind": {"type": "string"},
                    "namespace": {"type": "string"},
                    "labelSelector": {"type": "string"}
                  }
                }
              },
              "metrics": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Metrics to collect"
              }
            },
            "required": ["resources"]
          }
        }
      ]
    }
    ```

### API Testing Tools

* [REST API Tester](https://github.com/zenturacp/rest-api-tester)
  * Run: `npx @zenturacp/rest-api-tester-mcp`
  * Description: Comprehensive API testing and validation
  * Tool Definitions:
    ```json
    {
      "name": "api_tester",
      "description": "API testing and validation",
      "tools": [
        {
          "name": "test_endpoint",
          "description": "Test API endpoint",
          "parameters": {
            "type": "object",
            "properties": {
              "request": {
                "type": "object",
                "properties": {
                  "method": {"type": "string", "enum": ["GET", "POST", "PUT", "DELETE", "PATCH"]},
                  "url": {"type": "string"},
                  "headers": {"type": "object"},
                  "body": {"type": "object"}
                },
                "required": ["method", "url"]
              },
              "assertions": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "type": {"type": "string", "enum": ["status", "body", "header", "response_time"]},
                    "condition": {"type": "string"},
                    "value": {"type": "string"}
                  }
                }
              }
            },
            "required": ["request"]
          }
        },
        {
          "name": "generate_tests",
          "description": "Generate API tests from OpenAPI spec",
          "parameters": {
            "type": "object",
            "properties": {
              "spec": {"type": "string", "description": "OpenAPI specification"},
              "options": {
                "type": "object",
                "properties": {
                  "coverage": {"type": "string", "enum": ["basic", "full"]},
                  "environment": {"type": "string"},
                  "variables": {"type": "object"}
                }
              }
            },
            "required": ["spec"]
          }
        }
      ]
    }
    ```
* [WeCom Bot](https://github.com/loonghao/wecom-bot-mcp-server)
  * WeChat Work bot integration
  * Install: `pip install wecom-bot-mcp-server`

* [FeiShu Bot](https://github.com/loonghao/feishu-bot-mcp-server)
  * Feishu/Lark messaging platform integration
  * Install: `pip install feishu-bot-mcp-server`

* [JIRA Integration](https://github.com/Warzuponus/mcp-jira-python)
  * JIRA management with Scrum Master capabilities
  * Install: `pip install mcp-jira-python`

### Media Management
* [Music Manager](https://github.com/joeychilson/music-mcp)
  * Music library organization and management
  * Install: `pip install music-mcp`

* [MarkItDown Converter](https://github.com/KorigamiK/markitdown_mcp_server)
  * Convert various formats to Markdown
  * Install: `pip install markitdown-mcp-server`

## Additional Tools & Resources

### MCP Development Tools
* [MCP Registry](https://github.com/ARadRareness/mcp-registry) - Central registry for coordinating MCP servers
* [MCP Agent AI](https://github.com/mcpagents-ai/mcpagentai) - Python SDK for MCP server interactions
* [MCP Weather SSE](https://github.com/justjoehere/mcp-weather-sse) - Example server using Server-Sent Events

### Create Your Own Server
To create your own MCP server, you can:
1. Use the official SDKs (Python, TypeScript, or Kotlin)
2. Follow the [Model Context Protocol specification](https://modelcontextprotocol.io)
3. Start with example servers from the [quickstart resources](https://github.com/modelcontextprotocol/quickstart-resources)

### Implementations In Progress
Some servers listed in the directory are still in development or may be private implementations. The following services have been referenced but repositories are not yet publicly available:

* Docker Integration
* Shell/CLI Tools
* Build Automation Tools
* Terminal Emulators

If you're looking to implement these services, check the [MCP SDKs](#official-sdks) and [example implementations](#confirmed-packages--repositories) above.

## Official SDKs

* [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
* [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
* [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
* [Rust SDK (Unofficial)](https://github.com/jeanlucthumm/modelcontextprotocol-rust-sdk)
* [Go SDK (Unofficial)](https://github.com/jeanlucthumm/modelcontextprotocol-go-sdk)

## Development Tools

* [MCP Test Client](https://github.com/crazyrabbitLTC/mcp-test-client) - Testing utility for MCP servers
* [Mokei](https://github.com/TairuFramework/mokei) - TypeScript toolkit for creating and monitoring MCP clients/servers
* [MCP Server Runner](https://github.com/yonaka15/mcp-server-runner) - WebSocket server for running MCP servers

## Installation & Package Information

MCP servers can be installed and run using various package managers (npm, pip) or through direct GitHub repositories. Below is a list of available servers with their installation methods and source repositories where available.

## Application Servers

* [Gmail MCP Server](https://github.com/Ejb503/systemprompt-mcp-gmail)
  * Enables search, read, delete and send emails from Gmail
  * Install: `npm install @ejb503/systemprompt-mcp-gmail`

* [Twitch MCP](https://github.com/TomCools/twitch-mcp)
  * Connect to Twitch Chat through MCP
  * Install: `npm install @tomcools/twitch-mcp`

* [Keycloak MCP](https://github.com/ChristophEnglisch/keycloak-model-context-protocol)
  * User management through Keycloak
  * Install: `npm install @christophenglisch/keycloak-mcp`

* [Azure OpenAI Web Browser](https://github.com/kimtth/mcp-aoai-web-browsing)
  * Web browser control via Playwright with Azure OpenAI integration
  * Install: `npm install @kimtth/mcp-aoai-web-browsing`

* [Perplexity Server](https://github.com/PoliTwit1984/mcp-perplexity-server)
  * Code analysis and debugging using Perplexity AI
  * Install: `npm install @politwit1984/mcp-perplexity-server`

* [Crypto Price Server](https://github.com/truss44/mcp-crypto-price)
  * Real-time cryptocurrency analysis via CoinCap API
  * Install: `npm install @truss44/mcp-crypto-price`

* [Audiense Insights](https://github.com/AudienseCo/mcp-audiense-insights)
  * Interface with Audiense Insights analytics
  * Install: `npm install @audiense/mcp-insights`

* [Drupal Tools](https://github.com/Cleversoft-IT/drupal-tools-mcp)
  * Tools for Drupal development and Drush commands
  * Install: `npm install @cleversoft/drupal-tools-mcp`

## Categories Overview

MCP servers are organized into distinct categories based on their primary functions and use cases. Each category serves different integration needs for LLMs:

**Development & Coding Tools/Environments:**
Servers in this category provide LLMs with direct access to development environments, code execution capabilities, and programming tools. These enable AI models to write, test, and debug code, interact with various programming languages, and manage development workflows.

* **Docker:**
    * `https://www.pulsemcp.com/servers/quantgeekdev-docker-mcp`
    * GitHub: https://github.com/QuantGeekDev/docker-mcp
    * Installation: `npm install @quantgeekdev/docker-mcp`
* **Python REPL (Interactive Interpreter):**
    * `https://www.pulsemcp.com/servers/tynan-daly-python-repl`
    * `https://www.pulsemcp.com/servers/alec2435-python-local`
    * GitHub: https://github.com/what-the-func/mcp-python
    * Installation: `pip install mcp-python`
* **CLI (Command Line Interface) / Shell:**
    * `https://www.pulsemcp.com/servers/mladensu-cli-mcp-server`
    * `https://www.pulsemcp.com/servers/simonb97-windows-cli-mcp-server`
    * `https://www.pulsemcp.com/servers/tumf-mcp-shell-server`
    * `https://www.pulsemcp.com/servers/odysseus0-shell`
    * `https://www.pulsemcp.com/servers/hdresearch-shell`
* **Make (Build Automation):**
    * `https://www.pulsemcp.com/servers/wrale-makefile-make`
* **iTerm (Terminal Emulator):**
    * `https://www.pulsemcp.com/servers/ferrislucas-iterm`
* **Playwright (Browser Automation):**
    * `https://www.pulsemcp.com/servers/automata-labs-playwright`
* **Code Assistance:**
    * `https://www.pulsemcp.com/servers/abhishekbhakat-code-assist`
* **Codex Keeper (Code/Snippet Management):**
    * `https://www.pulsemcp.com/servers/aindreyway-codex-keeper`
* **OpenAPI Client Generator:**
    * Repository: [orhanveli/openapi-client-generator-mcp](https://github.com/orhanveli/openapi-client-generator-mcp)
      * Install: `npm install -g @orhanveli/openapi-client-generator-mcp`
      * Run: `npx openapi-client-generator-mcp`

**Database Servers:**
These servers provide secure access to various database management systems, allowing LLMs to query, analyze, and manipulate data while maintaining data security and integrity. They support both traditional relational databases and modern NoSQL solutions.

* **MongoDB:**
    * Repository: [kiliczsh/mcp-mongo-server](https://github.com/kiliczsh/mcp-mongo-server)
      * Install: `npm install -g @kiliczsh/mcp-mongo-server`
      * Run: `npx mcp-mongo-server`
* **MySQL:**
    * `https://www.pulsemcp.com/servers/benborla-mysql`
* **Redis:**
    * `https://www.pulsemcp.com/servers/farhankaz-redis`
* **Neo4j (Graph Database):**
    * `https://www.pulsemcp.com/servers/da-okazaki-neo4j`
* **SQLite:**
    * `https://www.pulsemcp.com/servers/johnnyoshika-sqlite-npx`
* **LibSQL (SQLite Compatible):**
    * `https://www.pulsemcp.com/servers/spences10-libsql-memory`

**API & Integration Tools:**
This category encompasses servers that connect LLMs with popular third-party services and platforms. These integrations enable AI models to interact with project management tools, content management systems, and other enterprise applications, streamlining workflows and automation.

* **Atlassian (Jira, Confluence etc.):**
    * Run: `npx @sooperset/atlassian-mcp`
    * Description: Comprehensive Atlassian platform integration
    * Tool Definitions:
    ```json
    {
      "name": "atlassian_operations",
      "description": "Atlassian platform operations",
      "tools": [
        {
          "name": "jira_issue",
          "description": "Manage Jira issues",
          "parameters": {
            "type": "object",
            "properties": {
              "operation": {
                "type": "string",
                "enum": ["create", "update", "get", "search"],
                "description": "Issue operation"
              },
              "projectKey": {"type": "string", "description": "Jira project key"},
              "issueData": {
                "type": "object",
                "properties": {
                  "summary": {"type": "string"},
                  "description": {"type": "string"},
                  "issueType": {"type": "string"},
                  "priority": {"type": "string"}
                }
              }
            },
            "required": ["operation", "projectKey"]
          }
        },
        {
          "name": "confluence_page",
          "description": "Manage Confluence pages",
          "parameters": {
            "type": "object",
            "properties": {
              "operation": {
                "type": "string",
                "enum": ["create", "update", "get", "delete"],
                "description": "Page operation"
              },
              "spaceKey": {"type": "string", "description": "Confluence space key"},
              "pageData": {
                "type": "object",
                "properties": {
                  "title": {"type": "string"},
                  "content": {"type": "string"},
                  "parentId": {"type": "string"}
                }
              }
            },
            "required": ["operation", "spaceKey"]
          }
        }
      ]
    }
    ```
* **DevRev (Developer CRM):**
    * Run: `npx @kpsunil97/devrev-mcp`
    * Description: DevRev integration for developer relationship management
    * Tool Definitions:
    ```json
    {
      "name": "devrev_operations",
      "description": "DevRev platform operations",
      "tools": [
        {
          "name": "create_issue",
          "description": "Create new issue in DevRev",
          "parameters": {
            "type": "object",
            "properties": {
              "title": {"type": "string", "description": "Issue title"},
              "body": {"type": "string", "description": "Issue description"},
              "priority": {
                "type": "string",
                "enum": ["p0", "p1", "p2", "p3"],
                "description": "Issue priority"
              },
              "tags": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Issue tags"
              }
            },
            "required": ["title", "body"]
          }
        },
        {
          "name": "manage_workflow",
          "description": "Manage DevRev workflow",
          "parameters": {
            "type": "object",
            "properties": {
              "workflowId": {"type": "string", "description": "Workflow ID"},
              "action": {
                "type": "string",
                "enum": ["start", "pause", "resume", "terminate"],
                "description": "Workflow action"
              },
              "parameters": {
                "type": "object",
                "additionalProperties": true,
                "description": "Workflow parameters"
              }
            },
            "required": ["workflowId", "action"]
          }
        },
        {
          "name": "query_metrics",
          "description": "Query DevRev metrics",
          "parameters": {
            "type": "object",
            "properties": {
              "metric": {"type": "string", "description": "Metric name"},
              "timeRange": {
                "type": "object",
                "properties": {
                  "start": {"type": "string"},
                  "end": {"type": "string"}
                }
              },
              "filters": {"type": "object", "description": "Query filters"}
            },
            "required": ["metric"]
          }
        }
      ]
    }
    ```
* **Jira (Issue Tracking):**
    * `https://www.pulsemcp.com/servers/alexeydubinin-hh-jira`
* **Linear (Issue Tracking):**
    * Run: `npx @shannonlal/linear-mcp`
    * Description: Linear project management and issue tracking integration
    * Tool Definitions:
    ```json
    {
      "name": "linear_operations",
      "description": "Linear project and issue management",
      "tools": [
        {
          "name": "create_issue",
          "description": "Create new Linear issue",
          "parameters": {
            "type": "object",
            "properties": {
              "teamId": {"type": "string", "description": "Team identifier"},
              "title": {"type": "string", "description": "Issue title"},
              "description": {"type": "string", "description": "Issue description"},
              "priority": {
                "type": "integer",
                "enum": [0, 1, 2, 3],
                "description": "Issue priority (0: none, 1: urgent, 2: high, 3: medium)"
              },
              "labels": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Issue labels"
              }
            },
            "required": ["teamId", "title"]
          }
        },
        {
          "name": "update_issue_status",
          "description": "Update Linear issue status",
          "parameters": {
            "type": "object",
            "properties": {
              "issueId": {"type": "string", "description": "Issue identifier"},
              "statusId": {"type": "string", "description": "New status identifier"},
              "comment": {"type": "string", "description": "Status update comment"}
            },
            "required": ["issueId", "statusId"]
          }
        },
        {
          "name": "query_issues",
          "description": "Query Linear issues",
          "parameters": {
            "type": "object",
            "properties": {
              "teamId": {"type": "string", "description": "Team identifier"},
              "filter": {
                "type": "object",
                "properties": {
                  "status": {"type": "string"},
                  "assignee": {"type": "string"},
                  "priority": {"type": "integer"},
                  "dueDate": {"type": "string"}
                }
              },
              "orderBy": {"type": "string", "description": "Sort field"}
            },
            "required": ["teamId"]
          }
        }
      ]
    }
    ```
* **Asana (Project Management):**
    * Run: `npx @roychri/asana-mcp`
    * Description: Asana project and task management integration
    * Tool Definitions:
    ```json
    {
      "name": "asana_operations",
      "description": "Asana project and task management",
      "tools": [
        {
          "name": "create_task",
          "description": "Create new Asana task",
          "parameters": {
            "type": "object",
            "properties": {
              "projectId": {"type": "string", "description": "Project identifier"},
              "name": {"type": "string", "description": "Task name"},
              "notes": {"type": "string", "description": "Task description"},
              "dueDate": {"type": "string", "description": "Due date (YYYY-MM-DD)"},
              "assignee": {"type": "string", "description": "Assignee email or ID"},
              "tags": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Task tags"
              }
            },
            "required": ["projectId", "name"]
          }
        },
        {
          "name": "manage_project",
          "description": "Manage Asana project",
          "parameters": {
            "type": "object",
            "properties": {
              "operation": {
                "type": "string",
                "enum": ["create", "update", "archive", "delete"],
                "description": "Project operation"
              },
              "projectData": {
                "type": "object",
                "properties": {
                  "name": {"type": "string"},
                  "notes": {"type": "string"},
                  "teamId": {"type": "string"},
                  "isPublic": {"type": "boolean"}
                }
              }
            },
            "required": ["operation", "projectData"]
          }
        },
        {
          "name": "search_tasks",
          "description": "Search Asana tasks",
          "parameters": {
            "type": "object",
            "properties": {
              "workspaceId": {"type": "string", "description": "Workspace identifier"},
              "projectId": {"type": "string", "description": "Project identifier"},
              "completed": {"type": "boolean", "description": "Task completion status"},
              "assignee": {"type": "string", "description": "Assignee filter"},
              "dueOn": {"type": "string", "description": "Due date filter"}
            },
            "required": ["workspaceId"]
          }
        }
      ]
    }
    ```
* **Airtable (Spreadsheet Database):**
    * Run: `npx @domdomegg/airtable-mcp`
    * Description: Airtable database integration and management
    * Tool Definitions:
    ```json
    {
      "name": "airtable_operations",
      "description": "Airtable database operations",
      "tools": [
        {
          "name": "query_records",
          "description": "Query Airtable records",
          "parameters": {
            "type": "object",
            "properties": {
              "baseId": {"type": "string", "description": "Airtable base ID"},
              "tableId": {"type": "string", "description": "Table ID or name"},
              "view": {"type": "string", "description": "View ID or name"},
              "fields": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Fields to return"
              },
              "filterByFormula": {"type": "string", "description": "Filter formula"},
              "sort": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "field": {"type": "string"},
                    "direction": {"type": "string", "enum": ["asc", "desc"]}
                  }
                }
              }
            },
            "required": ["baseId", "tableId"]
          }
        },
        {
          "name": "create_records",
          "description": "Create new Airtable records",
          "parameters": {
            "type": "object",
            "properties": {
              "baseId": {"type": "string", "description": "Airtable base ID"},
              "tableId": {"type": "string", "description": "Table ID or name"},
              "records": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "fields": {"type": "object", "description": "Record fields"}
                  }
                },
                "description": "Records to create"
              },
              "typecast": {"type": "boolean", "description": "Auto-convert field types"}
            },
            "required": ["baseId", "tableId", "records"]
          }
        },
        {
          "name": "update_records",
          "description": "Update existing Airtable records",
          "parameters": {
            "type": "object",
            "properties": {
              "baseId": {"type": "string", "description": "Airtable base ID"},
              "tableId": {"type": "string", "description": "Table ID or name"},
              "records": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "id": {"type": "string"},
                    "fields": {"type": "object", "description": "Fields to update"}
                  }
                }
              }
            },
            "required": ["baseId", "tableId", "records"]
          }
        }
      ]
    }
    ```
* **Contentful (CMS):**
    * Run: `npx @ivo-toby/contentful-mcp`
    * Description: Contentful content management system integration
    * Tool Definitions:
    ```json
    {
      "name": "contentful_operations",
      "description": "Contentful CMS management operations",
      "tools": [
        {
          "name": "get_entries",
          "description": "Retrieve Contentful entries",
          "parameters": {
            "type": "object",
            "properties": {
              "contentType": {"type": "string", "description": "Content type ID"},
              "query": {
                "type": "object",
                "properties": {
                  "limit": {"type": "integer"},
                  "skip": {"type": "integer"},
                  "order": {"type": "string"},
                  "select": {"type": "array", "items": {"type": "string"}},
                  "filter": {"type": "object"}
                }
              }
            },
            "required": ["contentType"]
          }
        },
        {
          "name": "create_entry",
          "description": "Create new Contentful entry",
          "parameters": {
            "type": "object",
            "properties": {
              "contentType": {"type": "string", "description": "Content type ID"},
              "fields": {
                "type": "object",
                "description": "Entry fields in specified locale"
              },
              "locale": {"type": "string", "description": "Content locale"},
              "publish": {"type": "boolean", "description": "Auto-publish entry"}
            },
            "required": ["contentType", "fields"]
          }
        },
        {
          "name": "manage_assets",
          "description": "Manage Contentful assets",
          "parameters": {
            "type": "object",
            "properties": {
              "operation": {
                "type": "string",
                "enum": ["upload", "process", "publish", "delete"],
                "description": "Asset operation"
              },
              "asset": {
                "type": "object",
                "properties": {
                  "title": {"type": "string"},
                  "description": {"type": "string"},
                  "file": {
                    "type": "object",
                    "properties": {
                      "url": {"type": "string"},
                      "fileName": {"type": "string"},
                      "contentType": {"type": "string"}
                    }
                  }
                }
              }
            },
            "required": ["operation", "asset"]
          }
        }
      ]
    }
    ```
* **API Connector (Generic):**
    * Run: `npx @jwaldor/api-connect-mcp`
    * Description: Generic API integration and connection management
    * Tool Definitions:
    ```json
    {
      "name": "api_connector",
      "description": "Generic API connection and management",
      "tools": [
        {
          "name": "request",
          "description": "Make API request",
          "parameters": {
            "type": "object",
            "properties": {
              "method": {
                "type": "string",
                "enum": ["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"],
                "description": "HTTP method"
              },
              "url": {"type": "string", "description": "API endpoint URL"},
              "headers": {
                "type": "object",
                "additionalProperties": {"type": "string"},
                "description": "Request headers"
              },
              "queryParams": {
                "type": "object",
                "additionalProperties": {"type": "string"},
                "description": "URL query parameters"
              },
              "body": {"type": "object", "description": "Request body"},
              "timeout": {"type": "integer", "description": "Request timeout (ms)"}
            },
            "required": ["method", "url"]
          }
        },
        {
          "name": "create_connection",
          "description": "Create reusable API connection",
          "parameters": {
            "type": "object",
            "properties": {
              "name": {"type": "string", "description": "Connection name"},
              "baseUrl": {"type": "string", "description": "Base API URL"},
              "auth": {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "enum": ["basic", "bearer", "apiKey", "oauth2"],
                    "description": "Authentication type"
                  },
                  "credentials": {"type": "object", "description": "Auth credentials"}
                }
              },
              "defaultHeaders": {"type": "object", "description": "Default headers"}
            },
            "required": ["name", "baseUrl"]
          }
        },
        {
          "name": "transform_response",
          "description": "Transform API response",
          "parameters": {
            "type": "object",
            "properties": {
              "response": {"type": "object", "description": "API response data"},
              "transformations": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "enum": ["extract", "map", "filter", "sort", "aggregate"],
                      "description": "Transformation type"
                    },
                    "config": {"type": "object", "description": "Transformation config"}
                  }
                }
              }
            },
            "required": ["response", "transformations"]
          }
        }
      ]
    }
    ```
* **REST API Tester:**
    * `https://www.pulsemcp.com/servers/zenturacp-rest-api-tester`
* **OpenAPI (Swagger) MCP Server:**
    * `https://www.pulsemcp.com/servers/snaggle-ai-openapi-mcp-server`
* **GitHub Pera (Likely GitHub API related):**
    * `https://www.pulsemcp.com/servers/kazuph-github-pera1`

**Cloud & Infrastructure Tools:**
Servers in this category facilitate interaction with cloud services and infrastructure management tools. They allow LLMs to manage containerized applications, serverless functions, and cloud resources, enabling automated infrastructure operations and deployments.

* **Kubernetes (Container Orchestration):**
    * `https://www.pulsemcp.com/servers/strowk-kubernetes`
* **Cloudflare Workers (Serverless Functions):**
    * `https://www.pulsemcp.com/servers/geelen-cloudflare-workers`

**LLM & AI Related:**
These servers enhance LLM capabilities through specialized AI tools and frameworks. They provide features like retrieval-augmented generation (RAG), context management, and AI framework integrations, enabling more sophisticated AI applications and improved model performance.

* **Langchain (LLM Framework):**
    * `https://www.pulsemcp.com/servers/rectalogic-langchain`
* **LLM Context:**
    * `https://www.pulsemcp.com/servers/restlessronin-llm-context`
* **AI/DD (Likely AI/Data & Decisions or similar):**
    * `https://www.pulsemcp.com/servers/skydeckai-aidd`
* **RAG Docs / Qdrant Docs RAG (Retrieval Augmented Generation for Documentation):**
    * `https://www.pulsemcp.com/servers/qpd-v-ragdocs`
    * `https://www.pulsemcp.com/servers/hannesrudolph-qdrant-docs-rag`
* **Command Executor (Potentially AI-driven command execution):**
    * `https://www.pulsemcp.com/servers/sunwood-ai-labs-command-executor`

**Utility & General Purpose Servers:**
This category includes a diverse collection of utility servers that provide common functionality needed across different applications. These servers handle tasks like time management, random number generation, file operations, and system utilities, serving as essential building blocks for more complex applications.

* **Time Server:**
    * Run: `npx @terminalman/timeserver-mcp`
    * Description: Time-related operations and scheduling
    * Tool Definitions:
    ```json
    {
      "name": "time_operations",
      "description": "Time and scheduling operations",
      "tools": [
        {
          "name": "get_time",
          "description": "Get current time in various formats",
          "parameters": {
            "type": "object",
            "properties": {
              "format": {
                "type": "string",
                "enum": ["iso", "unix", "human"],
                "description": "Time format"
              },
              "timezone": {"type": "string", "description": "Timezone"}
            }
          }
        },
        {
          "name": "schedule_task",
          "description": "Schedule a task",
          "parameters": {
            "type": "object",
            "properties": {
              "task": {"type": "string", "description": "Task to execute"},
              "time": {"type": "string", "description": "Schedule time"},
              "repeat": {"type": "boolean", "description": "Repeat task"}
            },
            "required": ["task", "time"]
          }
        }
      ]
    }
    ```
* **Random Number Generator:**
    * `https://www.pulsemcp.com/servers/turlockmike-rand`
* **Screenshot Tool:**
    * `https://www.pulsemcp.com/servers/sethbang-screenshot`
* **Package Version Checker:**
    * `https://www.pulsemcp.com/servers/sammcj-package-version`
* **Package Documentation Viewer:**
    * `https://www.pulsemcp.com/servers/sammcj-package-docs`
* **JSON Processing:**
    * Run: `npx @gongrzhe/json-mcp`
    * Description: JSON data manipulation and transformation
    * Tool Definitions:
    ```json
    {
      "name": "json_operations",
      "description": "JSON processing and transformation",
      "tools": [
        {
          "name": "transform",
          "description": "Transform JSON data",
          "parameters": {
            "type": "object",
            "properties": {
              "input": {"type": "object", "description": "Input JSON data"},
              "transformations": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "operation": {"type": "string", "enum": ["rename", "remove", "map", "filter"]},
                    "path": {"type": "string"},
                    "value": {"type": "string"}
                  }
                }
              }
            },
            "required": ["input", "transformations"]
          }
        },
        {
          "name": "validate",
          "description": "Validate JSON against schema",
          "parameters": {
            "type": "object",
            "properties": {
              "data": {"type": "object", "description": "JSON data to validate"},
              "schema": {"type": "object", "description": "JSON schema"}
            },
            "required": ["data", "schema"]
          }
        }
      ]
    }
    ```
* **Markdown Downloader:**
    * `https://www.pulsemcp.com/servers/dazeb-markdown-downloader`
* **NPM Search (Node Package Manager):**
    * `https://www.pulsemcp.com/servers/btwiuse-npm-search`
* **UI Flowchart Creator:**
    * `https://www.pulsemcp.com/servers/umshere-uiflowchartcreator`
* **cURL (HTTP Client):**
    * `https://www.pulsemcp.com/servers/mcp-get-curl`
* **macOS Utilities (Potentially system info or tools specific to macOS):**
    * `https://www.pulsemcp.com/servers/mcp-get-macos`
* **MCP to Serial (Serial Port Communication):**
    * `https://www.pulsemcp.com/servers/mcp2serial`
* **System Commands:**
    * `https://www.pulsemcp.com/servers/g0t4-system-commands`
* **Figma (Design Tool Integration):**
    * `https://www.pulsemcp.com/servers/matthewdailey-figma`
* **Shodan (Search Engine for Internet-connected devices):**
    * `https://www.pulsemcp.com/servers/burtthecoder-shodan`


**Note:**

* Some categories are based on educated guesses from the server descriptions. The exact tools and functionality within each server might vary.
* "MCP Server" in some descriptions likely refers to a server hosted on the PulseMCP platform itself and might not indicate a specific tool type beyond that.
*  "Generic MCP Server" category is omitted as most servers are "MCP Servers" in this list.