# Migration from AliceOS

On **May 1st, 2022**, the AliceOS project will cease development. It is highly
recommended that you migrate from AliceOS over to Candella, as it provides the
same feature set with extra enhancements and features to make your visual novel
game stand out.

## Full Announcement from Project Alice

Hello, fellow AliceOS developers! 👋🏻

For the past few years, AliceOS has remained a good framework used to provide an
operating system-like experience to visual novels and other games created in the
Ren'Py visual novel engine. We've been excited to see the project grow since its
initial technical previews in 2018 and taking a life of its own from the now outdated
_The Angel Returns_ project.

You'll have likely noticed development has stalled in most recent years, begging
whether AliceOS will continue development in the future. I'm writing this
announcement today to let you know that, on **May 1st, 2022**, the project will
officially cease development of the AliceOS project.

This was a hard decision to make. As developers, we love AliceOS and what it has been
capable of these past years. However, as we get involved with more projects,
maintaining AliceOS and its feature set has been rather difficult. As such, we felt
it is appropriate to cease development of AliceOS.

However, this does not mean that AliceOS is completely dead. There are a few options
available to developers:

- **Using AliceOS as-is**: Nothing is stopping you from using AliceOS Prospect Park
  as it stands today. Prospect Park is still a great release with a number of
  enhancements and improvements over the first release of AliceOS.

- **Making your own fork**: AliceOS remains a free and open-source solution under the
  BSD-2-Clause license, allowing you to make modifications to the AliceOS source code
  to fit your needs. We've seen a number of forks rise recently with additions for
  other languages and other features, and we're excited to see AliceOS live on in these
  forks.

  - **Using Candella**: [Candella](https://candella.unscriptedvn.dev) is a fork of
    AliceOS that adds features and enhancements we planned for the next release of
    AliceOS and provides a great experience for other developers with new APIs and an
    SDK. Although originally designed for Unscripted, it is actively maintained by
    some members of the AliceOS team (@alicerunsonfedora). We recommend migrating to
    Candella from AliceOS for a smooth experience.

### Sunsetting Strategy

With this in mind, we'll be doing the following on our end:

- **Archiving the AliceOS Repository**: We'll be archiving the repository and making
  it read-only; however, you can still fork a copy of the repository and make any
  adjustments you want on your fork. This will take effect immediately.
- **Shutting down aliceos.app**: As we recommend using Candella, we will be
  redirecting developers to the Candella documentation when visiting aliceos.app. We
  plan to shut down the aliceos.app domain by **July 7th, 2022**.

I'd personally like to thank the AliceOS development team, developers, and partners
for making AliceOS what it is today. While it is sad to see AliceOS go, I hope to see
it live on in the future through other forks like Candella.

\- Marquis Kurt (@alicerunsonfedora)

## How do I migrate?

If you're using AliceOS Prospect Park or later, simply delete `aliceos.rpa` and
follow the instructions in the [Getting Started](./01-getting-started.md) material.
There should be little friction when migrating your existing project over, as
Candella contains the same APIs and tools as AliceOS does.

If you do encounter any issues, file a support ticket on the Candella page at
[https://github.com/UnscriptedVN/candella/discussions/new?category=support-q-a](https://github.com/UnscriptedVN/candella/discussions/new?category=support-q-a).
