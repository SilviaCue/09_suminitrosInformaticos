
def importe_total_carro(request):
    total = 0
    if request.user.is_authenticated:
        if 'carro' in request.session:
            for key, value in request.session["carro"].items():
                total += float(value["precio"]) 
    else:
        total="Para continuear debes hacer login"
        
    return {"importe_total_carro": total}
