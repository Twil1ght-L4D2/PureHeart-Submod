# Pure Heart - submod registration

init 999 python:
    store.mas_submod_utils.Submod(
        author="Twilight",
        name="Pure Heart",
        version="1.9.0",
        description=(
            "A zero-tolerance content filter. Removes revealing outfits "
            "(bikinis, lingerie, towels, bare-shoulder tops), locks the "
            "risqué topics, and politely declines banned gift files. "
            "Hugs, kisses and snuggling closer are NOT touched."
        ),
    )

    store.pureheart_installed = True
