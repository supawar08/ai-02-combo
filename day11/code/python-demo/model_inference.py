# import required packages
import pickle

# load the model
with open("./adv-model.pkl", "rb") as file:

    # load the model in the memory
    # - deserialize the model
    model = pickle.load(file)

# make the inference (predict the sales using TV and radio budgets)
prediction = model.predict([[200, 40]])
print(prediction)