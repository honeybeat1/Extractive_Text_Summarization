# from transformers import AutoModel, AutoTokenizer
import torch


class rdass:
    def __init__(self, encoder, tokenizer):
        self.encoder = encoder
        self.tokenizer = tokenizer
        self.encoder.eval()

    def __call__(self, text=None, label=None, answer=None):
        with torch.no_grad():
            text_ids = self.tokenizer(
                text, truncation=True, max_length=512, return_tensors='pt')
            label_ids = self.tokenizer(label, return_tensors='pt')
            answer_ids = self.tokenizer(answer, return_tensors='pt')

            vector_text = self.encoder(
                **text_ids)['last_hidden_state']  # vector_d
            vector_label = self.encoder(
                **label_ids)['last_hidden_state']  # vector_r
            vector_answer = self.encoder(
                **answer_ids)['last_hidden_state']  # vector_p

        return get_score(vector_text[0, 0, :], vector_label[0, 0, :], vector_answer[0, 0, :])


def get_score(doc, label, answer):
    score_1 = torch.cosine_similarity(doc, answer, dim=0)
    score_2 = torch.cosine_similarity(label, answer, dim=0)
    return (score_1+score_2)/2

# tokenzier_for_eval = AutoTokenizer.from_pretrained("klue/roberta-small")
# model_for_eval = AutoModel.from_pretrained("klue/roberta-small")
# metric = rdass(model_for_eval,tokenzier_for_eval)
# score = metric(text,label,answer)
