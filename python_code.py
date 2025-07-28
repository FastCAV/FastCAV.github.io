import torchvision
from captum.concept import TCAV
from captum.attr import LayerIntegratedGradients
from fastcav import FastCAVCaptumClassifier

# Load your model
model = torchvision.models.googlenet(pretrained=True)
model = model.eval()

# Replace the default classifier with FastCAV
clf = FastCAVCaptumClassifier()
layers = ['inception4c', 'inception4d', 'inception4e']

# Use with TCAV as usual
tcav = TCAV(
    model=model,
    layers=layers,
    classifier=clf,  # Use FastCAV instead of default classifier
    layer_attr_method=LayerIntegratedGradients(
        model, None, multiply_by_inputs=False
    )
)

# Continue with your TCAV workflow...