
from django.http import JsonResponse
from itertools import combinations

# Create your views here.

def perm(request):

    s = request.GET.get("q")  
    out = []
    length = len(s)
    if length > 26:
        return JsonResponse({})
    c = 0
    for v in (combinations(s, (length+1)-i) for i in range(1, length+1) ):
        for j in set(v):
            out.append("".join(j))
            if c >= 100000:
                break
            c += 1
        if c >= 100000:
                break

    return JsonResponse(sorted(out, key=len, reverse=True), safe=False)
    




