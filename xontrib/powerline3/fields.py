import typing as tp
import builtins
import xonsh.built_ins as xb
from pathlib import Path

XSH = tp.cast(xb.XonshSession, builtins.__xonsh__)
XSH_ENV = XSH.env
XSH_FIELDS = XSH_ENV["PROMPT_FIELDS"]
XSH_FIELDS["time_format"] = "%I:%M:%S%p"


def add_as_field(f):
    XSH_FIELDS[f.__name__] = full_env_name


@add_as_field
def full_env_name():
    """When the `env_name` is
      - `.venv` show the name of the parent folder
      - contains `-py3.*` (when it is poetry created) shows the project name part alone

    Returns
    -------
    str
        python env_name
    """
    env_name: str = XSH_FIELDS["env_name"]()
    if env_name:
        venv_path = Path(XSH_ENV.get("VIRTUAL_ENV"))
        if venv_path.name == ".venv":
            return venv_path.parent.name
        if "-py" in env_name:
            name = venv_path.name.rsplit("-", 2)[0]
            return name

    return env_name


@add_as_field
def background_jobs():
    """Show number of background jobs"""
    num = 0
    for task in XSH.all_jobs.values():
        if task.get("bg"):
            num += 1

    return num if num else None


@add_as_field
def py_pkg_info():
    """Show package name and version if current directory has setup.py or pyproject.toml"""
    # todo
    return None


@add_as_field
def os_icon():
    """Show logo from nerd-fonts for current distro"""
    import distro

    # todo
    return None