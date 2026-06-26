import jetbrains.buildServer.configs.kotlin.v2019_2.*
import jetbrains.buildServer.configs.kotlin.v2019_2.buildSteps.python
import jetbrains.buildServer.configs.kotlin.v2019_2.triggers.vcs

version = "2019.2"

project {
    buildType(PythonDemo)
}

object PythonDemo : BuildType({
    name = "Python Demo"
    description = "TeamCity Python Demo Build"

    params {
        param("python.version", "3.11")
    }

    vcs {
        root(DslContext.settingsRoot)
    }

    steps {
        python {
            name = "Install dependencies"
            command = "-m pip install -r requirements.txt"
        }
        python {
            name = "Run unit tests"
            command = "-m pytest test_calculator.py -v --tb=short"
        }
        python {
            name = "Run tests with coverage"
            command = "-m pytest --cov=. --cov-report=xml --cov-report=html"
        }
    }

    triggers {
        vcs {
            branchFilter = ""
        }
    }

    artifactRules = """
        htmlcov/** => coverage.zip
        .coverage => coverage.zip
    """.trimIndent()
})
