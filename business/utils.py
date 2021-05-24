import uuid

def generate_unique_id(model):
	unique_id = uuid.uuid4()
	has_model = model.objects.filter(ID=unique_id).exists()
	if has_model:
		return generate_unique_id(model)
	return unique_id

