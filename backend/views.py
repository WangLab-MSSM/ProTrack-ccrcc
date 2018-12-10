import json

from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


@csrf_exempt
def index(request):
    return render(request, 'index.html')


@csrf_exempt
def submit_genes(request):
    if request.method == "POST":
        data = json.loads(request.body)
        genes = data['genes']

    all_genes = settings.ALL_GENES
    genes = [gene for gene in genes if gene in all_genes]

    sample_data = settings.CPTAC_DATA
    mutation = settings.MUTATION[genes]
    # cnv_baf = settings.CNV_BAF[genes]
    # cnv_lr = settings.CNV_LR[genes]
    # rna = settings.RNA[genes]
    # methylation = settings.METHYLATION[genes]
    # protein = settings.PROTEIN[genes]
    # phospho = settings.PHOSPHO[genes]

    sample_data = sample_data.to_json()
    mutation = mutation.to_json()
    # cnv_baf = cnv_baf.to_json()
    # cnv_lr = cnv_lr.to_json()
    # rna = rna.to_json()
    # methylation = methylation.to_json()
    # protein = protein.to_json()
    # phospho = phospho.to_json()

    return JsonResponse(
        {'sample_data': sample_data,
         'mutation': mutation,
         # 'cnv_baf': cnv_baf,
         # 'cnv_lr': cnv_lr,
         # 'rna': rna,
         # 'methylation': methylation,
         # 'protein': protein,
         # 'phospho': phospho
         },
        safe=False
    )
    # return render(request, 'index.html')
