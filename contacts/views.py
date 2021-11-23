from django.shortcuts import redirect
from .models import Contact
from django.core.mail import send_mail
from django.contrib import messages


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if user has already made inquiry
        if request.user.is_authenticated:
            has_made_inquiry = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_made_inquiry:
                messages.error(request, 'You have already made inquiry for this listing.')
                return redirect('/listings/' + listing_id)

        # If user is not authenticated we can do ip tracking...

        new_contact = Contact(listing_id=listing_id, listing=listing, email=email, name=name, phone=phone,
                              message=message, user_id=user_id)

        new_contact.save()

        # Send email
        send_mail(
            'Property Listing Inquiry',
            f'There has been inquiry for listing {listing}. Sign into the admin panel for more info.',
            'hhoybek@gmail.com',
            [realtor_email, 'hohoybek@gmail.com'],
            fail_silently=False
        )

        messages.success(request, 'Your request has been submitted, a realtor get back you soon.')
        return redirect('/listings/' + listing_id)
