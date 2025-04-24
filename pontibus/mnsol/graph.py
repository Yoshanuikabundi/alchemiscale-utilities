import pathlib

import click
import matplotlib.pyplot as plt
import numpy as np
import pandas
from openff.units import unit


@click.command
@click.option(
    "--results-file",
    type=click.Path(dir_okay=False, file_okay=True, path_type=pathlib.Path),
    required=True,
    default="results.dat",
    help="File location where the results TSV were written.",
)
def run(
    results_file: pathlib.Path,
):
    data = pandas.read_csv(results_file, sep="\t")

    # plot
    fig, axes = plt.subplots(1, 3)

    half_kt = (
        0.5
        * unit.boltzmann_constant
        * 298.15
        * unit.kelvin
        * unit.avogadro_constant
    ).m_as("kcal/mol")
    print(half_kt)
    for ax in axes:
        ax.set(
            xlim=(-15, 5),
            xticks=np.arange(-15, 5, 5),
            ylim=(-15, 5),
            yticks=np.arange(-15, 5, 2.5),
        )
        ax.axline(
            xy1=(0, 0),
            slope=1,
            color="black",
            dashes=(2, 2),
        )
        ax.axvline(
            x=0,
            color="black",
        )
        ax.axhline(
            y=0,
            color="black",
        )
        ax.fill_between(
            x=[-20, 10],
            y1=[-20 - half_kt, 10 - half_kt],
            y2=[-20 + half_kt, 10 + half_kt],
            color="grey",
            alpha=0.4,
        )

    axes[0].scatter(
        x=data["exp_dG (kcal/mol)"],
        y=data["calc_dG (kcal/mol)"],
        c=np.abs(data["calc_dG (kcal/mol)"]-data["exp_dG (kcal/mol)"]),
    )
    axes[0].set(
        xlabel="Pontibus ΔG (kcal/mol)",
        ylabel="Experiment ΔG (kcal/mol)",
    )

    axes[1].scatter(
        y=data["ref_dG (kcal/mol)"],
        x=data["calc_dG (kcal/mol)"],
        c=np.abs(data["calc_dG (kcal/mol)"]-data["ref_dG (kcal/mol)"]),
    )
    axes[1].set(
        xlabel="Pontibus ΔG (kcal/mol)",
        ylabel="Sage Reference ΔG (kcal/mol)",
    )

    axes[2].scatter(
        x=data["exp_dG (kcal/mol)"],
        y=data["ref_dG (kcal/mol)"],
        c=np.abs(data["ref_dG (kcal/mol)"]-data["exp_dG (kcal/mol)"]),
    )
    axes[2].set(
        xlabel="Sage Reference ΔG (kcal/mol)",
        ylabel="Experiment ΔG (kcal/mol)",
    )

    plt.show()


if __name__ == "__main__":
    run()
