
# Ports and adapters / hexagonal architecture
A toy example. In Django.

In this project I play with:
- writing ports and adapters code in a Django project
- writing a django project and turning it into a ports and adapters architecture.


## Books
The books app in this project was written as a domain model first and then brought in to Django.


## Libraries
This app was written as a Django project first. I intend to experiment with converting that to ports + adapters, probably via extracting Command objects from the views.

# Conclusion
Don't do this.

Django is built around the Active Record pattern and it's damaging to fight that. The need to isolate components is real but the boundary should be built around services, not around storage. A vertical slice architecture would be much more aligned to Django's opinions about project structure.
