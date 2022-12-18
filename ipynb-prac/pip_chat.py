# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Define constants for tax and insurance rates
import os.path
import pkgutil
import shutil
import tempfile
import importlib
from base64 import b85decode
import sys
import argparse
TAX_RATE = 0.22
INSURANCE_RATE = 0.07

# Define a function to calculate the salary for a full-time employee


def calculate_full_time_salary(hours, rate):
    # Calculate the gross salary
    gross_salary = hours * rate

    # Calculate the tax amount
    tax = gross_salary * TAX_RATE

    # Calculate the insurance amount
    insurance = gross_salary * INSURANCE_RATE

    # Calculate the net salary
    net_salary = ((gross_salary - tax) * 4) + 200

    return net_salary

# Define a function to calculate the salary for a part-time employee


def calculate_part_time_salary(hours, rate):
    # Calculate the gross salary
    gross_salary = hours * rate

    # Calculate the tax amount
    tax, insurance = gross_salary * TAX_RATE, 50

    # Calculate the net salary
    net_salary = ((gross_salary - tax) * 4) - insurance

    return net_salary


# Compare the salaries of full-time and part-time employees
full_time_hours = 40
full_time_rate = 17
monthy_hours_ft = (full_time_hours * 4) - 16
full_time_salary = calculate_full_time_salary(full_time_hours, full_time_rate)

part_time_hours = 25
monthy_hours_pt = part_time_hours * 4
part_time_rate = 17
part_time_salary = calculate_part_time_salary(part_time_hours, part_time_rate)

if full_time_salary > part_time_salary:
    print(f"The full-time employee has a higher salary at {full_time_salary} \
        and works {monthy_hours_ft} hours \
        the pt employee makes: {part_time_salary} \
        and works {monthy_hours_pt}.")
elif full_time_salary < part_time_salary:
    print("The part-time employee has a higher salary.")
else:
    print("The full-time and part-time employees have the same salary.")


# %%
print("full time salary: ", full_time_salary)


# %%
print("part time salary: ", part_time_salary)

# %% [markdown]
# ## Example argparse and pip programs to study

# %%


parser = argparse.ArgumentParser(
    description='sum the integers at the command line')
parser.add_argument(
    'integers', metavar='int', nargs='+', type=int,
    help='an integer to be summed')
parser.add_argument(
    '--log', default=sys.stdout, type=argparse.FileType('w'),
    help='the file where the sum should be written')
args = parser.parse_args()
args.log.write('%s' % sum(args.integers))
args.log.close()


# %%
# If you're wondering how this is created, it is generated using
# `scripts/generate.py` in https://github.com/pypa/get-pip.


this_python = sys.version_info[:2]
min_version = (3, 7)
if this_python < min_version:
    message_parts = [
        "This script does not work on Python {}.{}".format(*this_python),
        "The minimum supported Python version is {}.{}.".format(*min_version),
        "Please use https://bootstrap.pypa.io/pip/{}.{}/get-pip.py instead.".format(
            *this_python),
    ]
    print("ERROR: " + " ".join(message_parts))
    sys.exit(1)


def include_setuptools(args):
    """
    Install setuptools only if absent and not excluded.
    """
    cli = not args.no_setuptools
    env = not os.environ.get("PIP_NO_SETUPTOOLS")
    absent = not importlib.util.find_spec("setuptools")
    return cli and env and absent


def include_wheel(args):
    """
    Install wheel only if absent and not excluded.
    """
    cli = not args.no_wheel
    env = not os.environ.get("PIP_NO_WHEEL")
    absent = not importlib.util.find_spec("wheel")
    return cli and env and absent


def determine_pip_install_arguments():
    pre_parser = argparse.ArgumentParser()
    pre_parser.add_argument("--no-setuptools", action="store_true")
    pre_parser.add_argument("--no-wheel", action="store_true")
    pre, args = pre_parser.parse_known_args()

    args.append("pip")

    if include_setuptools(pre):
        args.append("setuptools")

    if include_wheel(pre):
        args.append("wheel")

    return ["install", "--upgrade", "--force-reinstall"] + args


def monkeypatch_for_cert(tmpdir):
    """Patches `pip install` to provide default certificate with the lowest priority.

    This ensures that the bundled certificates are used unless the user specifies a
    custom cert via any of pip's option passing mechanisms (config, env-var, CLI).

    A monkeypatch is the easiest way to achieve this, without messing too much with
    the rest of pip's internals.
    """
    from pip._internal.commands.install import InstallCommand

    # We want to be using the internal certificates.
    cert_path = os.path.join(tmpdir, "cacert.pem")
    with open(cert_path, "wb") as cert:
        cert.write(pkgutil.get_data("pip._vendor.certifi", "cacert.pem"))

    install_parse_args = InstallCommand.parse_args

    def cert_parse_args(self, args):
        if not self.parser.get_default_values().cert:
            # There are no user provided cert -- force use of bundled cert
            self.parser.defaults["cert"] = cert_path  # calculated above
        return install_parse_args(self, args)

    InstallCommand.parse_args = cert_parse_args


def bootstrap(tmpdir):
    monkeypatch_for_cert(tmpdir)

    # Execute the included pip and use it to install the latest pip and
    # setuptools from PyPI
    from pip._internal.cli.main import main as pip_entry_point
    args = determine_pip_install_arguments()
    sys.exit(pip_entry_point(args))


def main():
    tmpdir = None
    try:
        # Create a temporary working directory
        tmpdir = tempfile.mkdtemp()

        # Unpack the zipfile into the temporary directory
        pip_zip = os.path.join(tmpdir, "pip.zip")
        with open(pip_zip, "wb") as fp:
            fp.write(b85decode(DATA.replace(b"\n", b"")))

        # Add the zipfile to sys.path so that we can import it
        sys.path.insert(0, pip_zip)

        # Run the bootstrap
        bootstrap(tmpdir=tmpdir)
    finally:
        # Clean up our temporary working directory
        if tmpdir:
            shutil.rmtree(tmpdir, ignore_errors=True)
