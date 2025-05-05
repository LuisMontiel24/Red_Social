from django.shortcuts import render

# Create your views here.

def loginC(request):
    mensaje_error = None
    if request.method == 'POST':
        form = Formulario(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                usuario = Usuario.objects.get(email=email, password=password)
                request.session['usuario_id'] = usuario.id
                return redirect('inicio_sesion')
            except Usuario.DoesNotExist:
                mensaje_error = "Credenciales incorrectas"
    else:
        form = Formulario()

    return render(request, 'login.html', {
        'form': form,
        'mensaje_error': mensaje_error
    })



def inicio_sesion(request):
    usuario_id = request.session.get('usuario_id')
    if usuario_id:
        try:
            usuario = Usuario.objects.get(id=usuario_id)
            return render(request, 'inicioC.html', {
                'usuario': usuario,
            })
        except Usuario.DoesNotExist:
            if 'usuario_id' in request.session:
                del request.session['usuario_id']
            return redirect('loginC')
    else:
        return redirect('loginC')

def logout(request):
    if 'usuario_id' in request.session:
        del request.session['usuario_id']

    return redirect('loginC')