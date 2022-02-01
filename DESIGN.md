# gzip compression in NGINX

## Target Audiences

1. Maintenance and security teams
2. Training and technical support
3. Managers and other internal key stakeholders
4. Future project/feature owners/maintainers

## Detailed Summary

## Overall Intent

Enable gzip compression on NGINX servers.

### Piece 1 Intent

Allowing admins to adjust the gzip configuration.

### Piece 2 Intent

Allowing admins to adjust the gzip configuration.

### Piece 3 Intent

Mitigate or document BREACH attack of gzip over SSL/TLS.

Per [NGINX Docs](http://nginx.org/en/docs/http/ngx_http_gzip_module.html)

> When using the SSL/TLS protocol, compressed responses may be subject to [BREACH](https://en.wikipedia.org/wiki/BREACH) attacks.

## Maintainability

Estimate:

1. how much time and resources will be needed to maintain the feature in the future
   * very little, only one conf file involved
2. how frequently maintenance will need to happen
   * very infrequent, Only when our default config needs to change

## Options/Decisions

* enable and default configuration will go into /etc/nginx/conf.d/gzip.conf
* They can edit that file as they see fit
* Educate about BREACH
   * mitigate - its not really doable server side, Apache has a kludgey way (that we don’t do), NGINX doesn’t have the same mechanism so it’d be more kludgey if its even possible
   * document - even though gzip is a server things its really an app level problem. Would be better to encourage good practice

## Child Documents

None.
