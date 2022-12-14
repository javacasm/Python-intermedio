# Control de versiones: Git y github

El **control de versiones** es una herramienta esencial para el desarrollo de software en equipo, ya que permite llevar un registro de los cambios realizados en el código y facilitar la colaboración entre desarrolladores.

El control de versiones permite volver a versiones anteriores del código si es necesario, lo que puede ser útil en caso de errores o problemas en el código. También permite resolver conflictos de código cuando varios desarrolladores están trabajando en el mismo archivo al mismo tiempo.

Además, el control de versiones permite realizar pruebas y experimentos en una copia del código (**branch**) sin afectar la versión principal (**main**), lo que facilita la innovación y el desarrollo de nuevas funcionalidades.

También podemos mezclar (merge) nuestros cambios con los de otros desarrollaremos, para lo que git es capaz de detectar los distintos cambios y ver cómo se pueden mezclar sin que se pierdan ninguno de ellos. A veces pueden ocurrir conflictos, cuando el sistema no sabe realizar la mezcla de manera automática. En ese caso el desarrollador ha de proponer los cambios propuestos.

En resumen, el control de versiones es una herramienta esencial para el desarrollo de software en equipo y permite una gestión eficiente de cambios en los proyectos.

## Introducción

**Git** fue creado en 2005 por **Linus Torvalds**, el creador del sistema operativo **Linux**. La necesidad de un sistema de control de versiones eficiente surgió durante el desarrollo de Linux, ya que era necesario manejar el código de muchos desarrolladores de manera eficiente.



Torvalds desarrolló Git utilizando el lenguaje de programación C y basándose en un sistema anterior llamado BitKeeper. Git se convirtió en el sistema de control de versiones utilizado por el proyecto Linux y pronto fue adoptado por otros proyectos de software libre.



En 2008, se creó GitHub, una plataforma en línea para alojar proyectos utilizando Git y ofrecer herramientas colaborativas adicionales. GitHub se convirtió en una de las plataformas más populares para desarrolladores de software y en 2018 fue adquirida por Microsoft.

Git sigue siendo una de las herramientas más utilizadas por desarrolladores de software y es compatible con una amplia variedad de lenguajes de programación y sistemas operativos.

## Diferenicias entre git y github

Git es un sistema de control de versiones que permite a los desarrolladores de software llevar un registro de los cambios realizados en sus proyectos y colaborar con otros desarrolladores de manera eficiente.

Git almacena la historia de cada archivo del proyecto, permitiendo volver a versiones anteriores si es necesario, y brinda herramientas para resolver conflictos de código cuando se trabaja en equipo.

GitHub es una plataforma en línea que permite alojar proyectos utilizando Git y ofrece herramientas colaborativas adicionales como seguimiento de errores, discusiones y gestión de tareas.


## Instalación de git

Para utilizar Git y GitHub, primero se debe instalar Git en el equipo y crear una cuenta en GitHub.

Para instalar Git en un equipo con sistema operativo Windows, siga los siguientes pasos:

1. Descargue el instalador de Git desde el sitio web oficial: https://git-scm.com/download/win

1. Ejecute el instalador y siga las instrucciones en pantalla para completar la instalación.

1. Una vez finalizada la instalación, abra una consola de comandos (CMD) y verifique que Git está instalado correctamente utilizando el comando "git --version".

Para instalar Git en un equipo con sistema operativo Linux, siga los siguientes pasos:

1. Abra una consola de comandos y utilice el administrador de paquetes de su distribución Linux para instalar Git. Por ejemplo, en Ubuntu puede utilizar el comando "sudo apt install git".

1. Una vez finalizada la instalación, verifique que Git está instalado correctamente utilizando el comando "git --version".

Para instalar Git en un equipo con sistema operativo MacOS, siga los siguientes pasos:

1. Descargue el instalador de Git desde el sitio web oficial: https://git-scm.com/download/mac

1. Ejecute el instalador y siga las instrucciones en pantalla para completar la instalación.

1. Una vez finalizada la instalación, abra una consola de comandos (Terminal) y verifique que Git está instalado correctamente utilizando el comando "git --version".

En resumen, la instalación de Git varía según el sistema operativo utilizado, pero en general se trata de un proceso sencillo que puede realizarse siguiendo las instrucciones en pantalla del instalador.

## Uso

Un repositorio Git es un directorio en el que se almacena la historia de cambios de un proyecto utilizando Git. Un repositorio Git contiene todos los archivos del proyecto y sus versiones anteriores, así como información sobre quién realizó cada cambio y cuándo se realizó.

Para empezar a usar un repositorio se debe inicializar en el directorio local del proyecto utilizando el comando "**git init**".

Cada vez que se realice un cambio en el código, se deben agregar los archivos modificados al área de preparación utilizando el comando "**git add**" y luego guardar los cambios en la historia del repositorio con el comando "git commit".

Para colaborar en un proyecto, se puede clonar el repositorio desde GitHub utilizando el comando "**git clone url-repositorio**" y luego realizar cambios localmente. Una vez que los cambios estén listos, se pueden enviar al repositorio remoto utilizando el comando "git push".

Si en algún momento queremos descargar las actualizaciones que otros desarrolladores han hecho en el repositorio haremos "**git pull**" y se descargarán los cambios, mezclándose con los nuestros.

### Resolución de conflictos

Cuando varios desarrolladores están trabajando en el mismo archivo de código al mismo tiempo, es posible que se generen conflictos al enviar los cambios al repositorio remoto. Estos conflictos se deben resolver manualmente para evitar problemas en el código.

Para resolver conflictos con Git, siga los siguientes pasos:

1. Realice un **git pull** del repositorio remoto para obtener la última versión del código y evitar conflictos.

1. Realice los cambios en el archivo de código que desee.

1. Realice un commit de los cambios utilizando un mensaje claro y descriptivo.

1. Realice un push del código al repositorio remoto. Si se genera un conflicto, Git mostrará un mensaje de error y detendrá el proceso.

1. Abra el archivo donde se generó el conflicto y busque las líneas que comienzan con "<<<<<<<" y ">>>>>>>". Estas líneas marcan el inicio y el fin del conflicto.

1. Elimine las líneas que marcan el inicio y el fin del conflicto y resuelva el conflicto de manera manual. Por ejemplo, si se trata de un cambio en una línea de código, puede elegir qué versión utilizar

1. Realice un commit y un push del archivo resuelto para enviar los cambios al repositorio remoto.

1. Verifique que el conflicto ha sido resuelto correctamente en el repositorio remoto.

En resumen, resolver conflictos con Git requiere un proceso manual que implica identificar el conflicto, resolverlo de manera manual y luego enviar los cambios al repositorio remoto. Es importante utilizar mensajes claros y descriptivos en los commits y realizar un pull del repositorio remoto antes de realizar cambios para evitar conflictos.


## Autentificación en github

Para modificar nuestros repositorios en github necesitamos autintificarnos con nuestra cuenta. GitHub ofrece dos opciones para conectarse a un repositorio remoto: HTTP y SSH.

La opción HTTP utiliza el protocolo HTTP para comunicarse con el repositorio remoto y requiere que se ingrese el nombre de usuario y la contraseña de la cuenta de GitHub cada vez que se realice un push o un pull del repositorio.

La opción SSH utiliza el protocolo SSH para comunicarse con el repositorio remoto y requiere que se genere y agregue una clave SSH a la cuenta de GitHub. Una vez que se agrega la clave, no es necesario ingresar el nombre de usuario y la contraseña cada vez que se realice un push o un pull del repositorio.

En resumen, ambas opciones son válidas para conectarse a un repositorio remoto en GitHub, pero la opción SSH es más segura y cómoda ya que no requiere ingresar el nombre de usuario y la contraseña cada vez.

### Acceso a github con ssh

Para utilizar la opción SSH en GitHub, es necesario generar una clave SSH y agregarla a la cuenta de GitHub. Para generar una clave SSH, siga los siguientes pasos:

Abra una consola de comandos y ejecute el comando "ssh-keygen".

Siga las instrucciones en pantalla para generar la clave SSH. Es importante recordar la contraseña que se ingresa al generar la clave.

Una vez generada la clave, utilice el comando "cat" para ver el contenido de la clave pública, que comienza con "ssh-rsa". Por ejemplo, si la clave se guardó en el archivo "id_rsa.pub", se puede utilizar el comando "cat id_rsa.pub".

Copie el contenido de la clave pública y vaya a la página de configuración de SSH en su cuenta de GitHub.

En la página de configuración de SSH, haga clic en "Add SSH key" y pegue el contenido de la clave pública en el campo correspondiente.

Ingrese un título para la clave y haga clic en "Add SSH key" para agregarla a su cuenta de GitHub.

Una vez que la clave SSH está agregada a su cuenta de GitHub, ya no es necesario ingresar el nombre de usuario y la contraseña cada vez que se realice un push o un pull del repositorio. La clave SSH se utiliza para autenticar la conexión y permitir el acceso al repositorio.

Es importante tener en cuenta que la clave SSH debe ser protegida de manera adecuada ya que permite el acceso a los repositorios privados. Se recomienda utilizar una contraseña segura al generar la clave y no compartir la clave con personas no autorizadas.

En resumen, la firma SSH es una clave generada para autenticar la conexión con un repositorio remoto en GitHub y evitar la necesidad de ingresar el nombre de usuario y la contraseña cada vez que se realice un push o un pull. Es importante proteger adecuadamente la clave SSH para garantizar la seguridad del repositorio.

## Repositorios públicos y privados en github

GitHub ofrece la posibilidad de crear repositorios públicos o privados.

Un repositorio público es accesible por cualquier persona y puede ser clonado y utilizado libremente. Los repositorios públicos son útiles para proyectos de código abierto y para compartir código con otros desarrolladores.

Un repositorio privado solo es accesible por los usuarios autorizados y requiere una invitación para ser clonado. Los repositorios privados son útiles para proyectos que deben mantenerse en privado, como proyectos comerciales o proyectos de investigación.

En resumen, GitHub ofrece la opción de crear repositorios públicos o privados según las necesidades del proyecto. Los repositorios públicos son accesibles por cualquier persona y los repositorios privados solo son accesibles por usuarios autorizados.

## Recursos

[Documentación](https://docs.github.com/es/get-started/quickstart/hello-world)
