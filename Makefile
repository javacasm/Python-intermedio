
S4  = "4. Programación de aplicaciones de escritorio.docx"
S5  = "5. Automatización de tareas del sistema.docx"
SA  = "Apéndice. Uso de Git y Github.docx"


4:
	pandoc --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		--reference-doc=plantilla-intermedio.docx \
		-o  $(S4)  \
		Cabecera.md        \
		Cabecera_latex.md \
		4.0.app-ui.md \
		4.1.app-ui-tkinter.md

5:
	pandoc --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		--reference-doc=plantilla-intermedio.docx \
		-o  $(S5)  \
		Cabecera.md        \
		Cabecera_latex.md \
		5.0.Automatizacion.md \
		5.1.scheduler.md \
		5.2.web_scrapping_beautifulsoup.md

A:
	pandoc --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		--reference-doc=plantilla-intermedio.docx \
		-o  $(SA)  \
		Cabecera.md        \
		Cabecera_latex.md \
		A.git-github.md
		