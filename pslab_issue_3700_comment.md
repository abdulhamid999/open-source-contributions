Hi @hypertonny and maintainers,

I investigated this issue and traced the root cause:

1. The issue stems from the physical flyer on display at the Devcon booth (seen in the screenshot), where the printed QR code points to `https://pslab.io/order`.
2. Requesting `https://pslab.io/order` returns an **HTTP 404 Not Found** on the Apache server at `pslab.io`, whereas the working shop route is `https://pslab.io/shop/`.
3. Because the URL is physically printed on distributed paper flyers, it cannot be fixed via code changes in the Flutter `pslab-app` mobile repository.

To resolve this immediately for event attendees scanning the flyer, a server-level redirect (e.g. via Cloudflare Page Rules or Apache `.htaccess` rewrite) needs to be configured on the `pslab.io` host to redirect `/order` -> `/shop/` (or the intended pre-order campaign URL).

