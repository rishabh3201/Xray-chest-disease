from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np

def disease(filename):
    model = load_model('model_vgg19_new.h5')
    img = image.load_img(f'Datasets1/val/validation/{filename}',target_size=(224,224))
    x = image.img_to_array(img)
    x = np.expand_dims(x,axis=0)
    img_data = preprocess_input(x)
    classes = model.predict(img_data)
    threshold = 0.5
    class_names = ['Normal', 'Edema', 'Cardiomegaly', 'Effusion', 'Infiltration', 'Mass',
               'Nodule', 'Pneumonia', 'Pneumothorax','Fibrosis', 'Atelectasis', 
               'Emphysema', 'Consolidation', 'Pleural_Thickening', 'Hernia']

    predicted_class_index = np.argmax(classes)
    predicted_probability = classes[0][predicted_class_index]

    predicted_disease = class_names[predicted_class_index]
    return predicted_disease
    # if classes[0][0] < threshold:
    #     return "Pneumonia"
    # else:
    #     return "Normal"

    # classes_int = classes.astype(int)
    # print(classes[0][1])
    # print(img)
    # return "Pneumonia"
# model = load_model('model_vgg19.h5')
# img = image.load_img('Datasets/val/check/Atelectasis.Effusion.Pleural_Thickening.00012520_002.png',target_size=(224,224))
# x = image.img_to_array(img)
# x = np.expand_dims(x,axis=0)
# img_data = preprocess_input(x)
# classes = model.predict(img_data)

# class_names = ['Normal', 'Edema', 'Cardiomegaly', 'Effusion', 'Infiltration', 'Mass',
#                'Nodule', 'Pneumonia', 'Pneumothorax','Fibrosis', 'Atelectasis', 
#                'Emphysema', 'Consolidation', 'Pleural_Thickening', 'Hernia']

# # Find the index of the class with the highest probability
# predicted_class_index = np.argmax(classes)
# predicted_probability = classes[0][predicted_class_index]

# # Get the name of the predicted disease
# predicted_disease = class_names[predicted_class_index]

# # Print the predicted class and its probability
# print(f"Predicted Class Index: {predicted_class_index}")
# print(f"Predicted Disease: {predicted_disease}")
# print(f"Predicted Probability: {predicted_probability}")

# threshold = 0.5
# total_sum = np.sum(classes)
# print(f"Total Sum of the Values: {total_sum}")

# # Threshold to predict the presence of disease
# threshold = 0.5

# # If you want to predict based on the highest probability
# predicted_class_index = np.argmax(classes)
# predicted_probability = classes[0][predicted_class_index]

# # Mapping of class indices to disease names (example, replace with your actual class names)
# class_names = ['Normal', 'Edema', 'Cardiomegaly', 'Effusion', 'Infiltration', 'Mass',
#                'Nodule', 'Pneumonia', 'Pneumothorax', 'Consolidation', 'Atelectasis', 
#                'Emphysema', 'Fibrosis', 'Pleural_Thickening', 'Hernia']

# predicted_disease = class_names[predicted_class_index]

# # Print the predicted class and its probability
# print(f"Predicted Class Index: {predicted_class_index}")
# print(f"Predicted Disease: {predicted_disease}")
# print(f"Predicted Probability: {predicted_probability}")

# # You can also check against the threshold if you want to determine disease presence
# if predicted_probability > threshold:
#     print(f"The model predicts the presence of {predicted_disease} with a probability of {predicted_probability}.")
# else:
#     print(f"The model does not predict {predicted_disease} with a high probability.")
# if classes[0][0] < threshold:
#     print("Pneumonia")
# else:
#     print("Normal")
