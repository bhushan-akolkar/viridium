#from django.shortcuts import render
from django.http import JsonResponse
# from ChunksExtraction import ChunksExtraction
 # from ChunksExtraction import ChunksExtraction
from p_app.ChunksExtraction import ChunksExtraction
# from ChunksExtraction import ChunksExtraction
import json

chunks = ChunksExtraction()

    
def get_chunks(request):

    if request.method == 'GET':
        data = json.loads(request.body)
        question = data['question']
        vectorstore = chunks.get_Vectorstore('/home/user/LLM/FAISS/text-embeddings-ada-002-2500-250')
        # chunk = chunks.get_chunks(vectorstore,question)
        context = []
        chunk = chunks.get_chunks(vectorstore,question)
        for i in chunk:
            a=dict(i)
            context.append({'context_text': a['page_content'], 'metadata': a['metadata']})
        return JsonResponse({"status": "SUCCESS", "response": context})

    
