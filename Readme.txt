El proyecto se llama Entrega3. La app es una tienda de bicicletas de momento con las siguientes clases:
	- Modelo bicicletas
	- Accesorios
	- Clientes

Dentro de la App tengo una plágina de incio.
La página de inicio de Entrega3 es el template padre: base.html (http://localhost:8000/inicio/)

Los forumularios los implementé de forma diferente. Para Accesorio y Cliente lo hice con un objeto Form. Para Modelo bicicleta lo hice de la forma larga.
Esto fue así ya que con el objeto Form no me funcionaba y fui solucionando otros errores con la página de forumulario de Modelo bicicleta. 
Finalmente encontré en foros que el problema era pasarle a la página la clase formulario y no la instancia (
