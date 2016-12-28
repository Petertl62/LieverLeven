from django.db import models


class Contact(models.Model):
    """
    Contact Message
    Fields: Firstname, Lastname,
            Email, Birthday, Gender, Company,
            Timestamp, Updated Timestamp, Title, Content
    - The minimal requirements for a Contact Message
    """
    GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('P', 'Prefer not to say'),
    )

    # Personel Information
    firstname   = models.CharField(max_length=32)
    lastname    = models.CharField(max_length=64)
    # Street        : Optionel, Not Saved to DB
    # Zipcode       : Optionel, Not Saved to DB
    # residence     : Optionel, Not Saved to DB
    # country       : Optionel, Not Saved to DB

    # Extended Information
    email       = models.EmailField()
    birthday    = models.DateField(blank=True) # Optionel
    gender      = models.CharField(max_length=1, blank=True,choices=GENDER_CHOICES)
    company     = models.CharField(max_length=64, blank=True) # Optionel
    # Phone number  : Optionel, Not Saved to DB

    # Contact Message Posting Information
    timestamp   = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True, auto_now_add=False)
    title       = models.CharField(max_length=128)
    content     = models.TextField()

    def __str__(self):
        """
        String: Timestamp || Firstname Lastname, Email
        - The return value for administration purposes
        """
        return "%s || %s %s, %s" %(
            self.timestamp,
            self.firstname,
            self.lastname,
            self.email,
        )

    class Meta:
        """
        Meta: get_latest_by, ordering, verbose_name, verbose_name_plural
        - Ordering declaration for the database
        - Naming for administration purposes
        """
        get_latest_by       = "timestamp"
        ordering            = ["-timestamp"]
        verbose_name        = "Contact Message"
        verbose_name_plural = "Contact Messeges"
