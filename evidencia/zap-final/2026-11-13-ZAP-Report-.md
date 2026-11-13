# zap_final

ZAP by [Checkmarx](https://checkmarx.com/).


## Summary of Alerts

| Risk Level | Number of Alerts |
| --- | --- |
| High | 0 |
| Medium | 2 |
| Low | 4 |
| Informational | 4 |




## Insights

| Level | Reason | Site | Description | Statistic |
| --- | --- | --- | --- | --- |
| Low | Warning |  | ZAP warnings logged - see the zap.log file for details | 3    |
| Info | Informational | http://127.0.0.1:8000 | Percentage of responses with status code 2xx | 56 % |
| Info | Informational | http://127.0.0.1:8000 | Percentage of responses with status code 3xx | 34 % |
| Info | Informational | http://127.0.0.1:8000 | Percentage of responses with status code 4xx | 9 % |
| Info | Informational | http://127.0.0.1:8000 | Percentage of endpoints with content type text/css | 5 % |
| Info | Informational | http://127.0.0.1:8000 | Percentage of endpoints with content type text/html | 95 % |
| Info | Informational | http://127.0.0.1:8000 | Percentage of endpoints with method GET | 60 % |
| Info | Informational | http://127.0.0.1:8000 | Percentage of endpoints with method POST | 40 % |
| Info | Informational | http://127.0.0.1:8000 | Count of total endpoints | 20    |
| Info | Informational | http://127.0.0.1:8000 | Percentage of slow responses | 13 % |
| Info | Informational | https://edge-consumer-static.azureedge.net | Percentage of responses with status code 2xx | 100 % |
| Info | Informational | https://edge-consumer-static.azureedge.net | Percentage of endpoints with content type application/json | 100 % |
| Info | Informational | https://edge-consumer-static.azureedge.net | Percentage of endpoints with method GET | 100 % |
| Info | Informational | https://edge-consumer-static.azureedge.net | Count of total endpoints | 1    |
| Info | Informational | https://editor.svc.cloud.microsoft | Percentage of responses with status code 2xx | 100 % |
| Info | Informational | https://editor.svc.cloud.microsoft | Percentage of endpoints with content type application/json | 100 % |
| Info | Informational | https://editor.svc.cloud.microsoft | Percentage of endpoints with method POST | 100 % |
| Info | Informational | https://editor.svc.cloud.microsoft | Count of total endpoints | 1    |
| Info | Informational | https://editor.svc.cloud.microsoft | Percentage of slow responses | 33 % |
| Info | Informational | https://xpaywalletcdn-prod.azureedge.net | Percentage of responses with status code 2xx | 100 % |
| Info | Informational | https://xpaywalletcdn-prod.azureedge.net | Percentage of endpoints with content type text/plain | 100 % |
| Info | Informational | https://xpaywalletcdn-prod.azureedge.net | Percentage of endpoints with method GET | 100 % |
| Info | Informational | https://xpaywalletcdn-prod.azureedge.net | Count of total endpoints | 1    |
| Info | Informational | https://xpaywalletcdn-prod.azureedge.net | Percentage of slow responses | 100 % |







## Alerts

| Name | Risk Level | Number of Instances |
| --- | --- | --- |
| Content Security Policy (CSP) Header Not Set | Medium | Systemic |
| Cross-Domain Misconfiguration | Medium | 2 |
| Cookie No HttpOnly Flag | Low | Systemic |
| Server Leaks Version Information via "Server" HTTP Response Header Field | Low | 1 |
| Strict-Transport-Security Header Not Set | Low | 1 |
| X-Content-Type-Options Header Missing | Low | 2 |
| Authentication Request Identified | Informational | 2 |
| Re-examine Cache-control Directives | Informational | 2 |
| Session Management Response Identified | Informational | 14 |
| User Controllable HTML Element Attribute (Potential XSS) | Informational | 4 |




## Alert Detail



### [ Content Security Policy (CSP) Header Not Set ](https://www.zaproxy.org/docs/alerts/10038/)



##### Medium (High)

### Description

Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.

* URL: http://127.0.0.1:8000/
  * Node Name: `http://127.0.0.1:8000/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://127.0.0.1:8000/login/%3Fnext=/
  * Node Name: `http://127.0.0.1:8000/login/ (next)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://127.0.0.1:8000/producto/2/
  * Node Name: `http://127.0.0.1:8000/producto/2/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://127.0.0.1:8000/producto/nuevo/
  * Node Name: `http://127.0.0.1:8000/producto/nuevo/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://127.0.0.1:8000/login/%3Fnext=/producto/2/
  * Node Name: `http://127.0.0.1:8000/login/ (next)(csrfmiddlewaretoken,password,username)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``

Instances: Systemic


### Solution

Ensure that your web server, application server, load balancer, etc. is configured to set the Content-Security-Policy header.

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)
* [ https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html ](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
* [ https://www.w3.org/TR/CSP/ ](https://www.w3.org/TR/CSP/)
* [ https://w3c.github.io/webappsec-csp/ ](https://w3c.github.io/webappsec-csp/)
* [ https://web.dev/articles/csp ](https://web.dev/articles/csp)
* [ https://caniuse.com/#feat=contentsecuritypolicy ](https://caniuse.com/#feat=contentsecuritypolicy)
* [ https://content-security-policy.com/ ](https://content-security-policy.com/)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 15

#### Source ID: 3

### [ Cross-Domain Misconfiguration ](https://www.zaproxy.org/docs/alerts/10098/)



##### Medium (Medium)

### Description

Web browser data loading may be possible, due to a Cross Origin Resource Sharing (CORS) misconfiguration on the web server.

* URL: http://127.0.0.1:8000/static/css/dist/styles.css
  * Node Name: `http://127.0.0.1:8000/static/css/dist/styles.css`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `Access-Control-Allow-Origin: *`
  * Other Info: `The CORS misconfiguration on the web server permits cross-domain read requests from arbitrary third party domains, using unauthenticated APIs on this domain. Web browser implementations do not permit arbitrary third parties to read the response from authenticated APIs, however. This reduces the risk somewhat. This misconfiguration could be used by an attacker to access data that is available in an unauthenticated manner, but which uses some other form of security, such as IP address white-listing.`
* URL: https://edge-consumer-static.azureedge.net/mouse-gesture/config.json
  * Node Name: `https://edge-consumer-static.azureedge.net/mouse-gesture/config.json`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `Access-Control-Allow-Origin: *`
  * Other Info: `The CORS misconfiguration on the web server permits cross-domain read requests from arbitrary third party domains, using unauthenticated APIs on this domain. Web browser implementations do not permit arbitrary third parties to read the response from authenticated APIs, however. This reduces the risk somewhat. This misconfiguration could be used by an attacker to access data that is available in an unauthenticated manner, but which uses some other form of security, such as IP address white-listing.`


Instances: 2

### Solution

Ensure that sensitive data is not available in an unauthenticated manner (using IP address white-listing, for instance).
Configure the "Access-Control-Allow-Origin" HTTP header to a more restrictive set of domains, or remove all CORS headers entirely, to allow the web browser to enforce the Same Origin Policy (SOP) in a more restrictive manner.

### Reference


* [ https://vulncat.fortify.com/en/detail?category=HTML5&subcategory=Overly%20Permissive%20CORS%20Policy ](https://vulncat.fortify.com/en/detail?category=HTML5&subcategory=Overly%20Permissive%20CORS%20Policy)


#### CWE Id: [ 264 ](https://cwe.mitre.org/data/definitions/264.html)


#### WASC Id: 14

#### Source ID: 3

### [ Cookie No HttpOnly Flag ](https://www.zaproxy.org/docs/alerts/10010/)



##### Low (Medium)

### Description

A cookie has been set without the HttpOnly flag, which means that the cookie can be accessed by JavaScript. If a malicious script can be run on this page then the cookie will be accessible and can be transmitted to another site. If this is a session cookie then session hijacking may be possible.

* URL: http://127.0.0.1:8000/
  * Node Name: `http://127.0.0.1:8000/`
  * Method: `GET`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `Set-Cookie: csrftoken`
  * Other Info: ``
* URL: http://127.0.0.1:8000/login/%3Fnext=/
  * Node Name: `http://127.0.0.1:8000/login/ (next)`
  * Method: `GET`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `Set-Cookie: csrftoken`
  * Other Info: ``
* URL: http://127.0.0.1:8000/producto/nuevo/
  * Node Name: `http://127.0.0.1:8000/producto/nuevo/`
  * Method: `GET`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `Set-Cookie: csrftoken`
  * Other Info: ``
* URL: http://127.0.0.1:8000/login/%3Fnext=/producto/2/
  * Node Name: `http://127.0.0.1:8000/login/ (next)(csrfmiddlewaretoken,password,username)`
  * Method: `POST`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `Set-Cookie: csrftoken`
  * Other Info: ``
* URL: http://127.0.0.1:8000/producto/nuevo/
  * Node Name: `http://127.0.0.1:8000/producto/nuevo/ ()(csrfmiddlewaretoken,descripcion,nombre,precio,stock)`
  * Method: `POST`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `Set-Cookie: csrftoken`
  * Other Info: ``

Instances: Systemic


### Solution

Ensure that the HttpOnly flag is set for all cookies.

### Reference


* [ https://owasp.org/www-community/HttpOnly ](https://owasp.org/www-community/HttpOnly)


#### CWE Id: [ 1004 ](https://cwe.mitre.org/data/definitions/1004.html)


#### WASC Id: 13

#### Source ID: 3

### [ Server Leaks Version Information via "Server" HTTP Response Header Field ](https://www.zaproxy.org/docs/alerts/10036/)



##### Low (High)

### Description

The web/application server is leaking version information via the "Server" HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.

* URL: https://editor.svc.cloud.microsoft/NLEditor/TileCheck/V1
  * Node Name: `https://editor.svc.cloud.microsoft/NLEditor/TileCheck/V1 ()({SessionId,AppId,LanguageUxId,Content:[{TileId,RevisionId,TileElements:[{LanguageId,Text,TextUnit}]}],Descriptors:[{Name,Value}..]})`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `Microsoft-HTTPAPI/2.0`
  * Other Info: ``


Instances: 1

### Solution

Ensure that your web server, application server, load balancer, etc. is configured to suppress the "Server" header or provide generic details.

### Reference


* [ https://httpd.apache.org/docs/current/mod/core.html#servertokens ](https://httpd.apache.org/docs/current/mod/core.html#servertokens)
* [ https://learn.microsoft.com/en-us/previous-versions/msp-n-p/ff648552(v=pandp.10) ](https://learn.microsoft.com/en-us/previous-versions/msp-n-p/ff648552(v=pandp.10))
* [ https://www.troyhunt.com/shhh-dont-let-your-response-headers/ ](https://www.troyhunt.com/shhh-dont-let-your-response-headers/)


#### CWE Id: [ 497 ](https://cwe.mitre.org/data/definitions/497.html)


#### WASC Id: 13

#### Source ID: 3

### [ Strict-Transport-Security Header Not Set ](https://www.zaproxy.org/docs/alerts/10035/)



##### Low (High)

### Description

HTTP Strict Transport Security (HSTS) is a web security policy mechanism whereby a web server declares that complying user agents (such as a web browser) are to interact with it using only secure HTTPS connections (i.e. HTTP layered over TLS/SSL). HSTS is an IETF standards track protocol and is specified in RFC 6797.

* URL: https://edge-consumer-static.azureedge.net/mouse-gesture/config.json
  * Node Name: `https://edge-consumer-static.azureedge.net/mouse-gesture/config.json`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``


Instances: 1

### Solution

Ensure that your web server, application server, load balancer, etc. is configured to enforce Strict-Transport-Security.

### Reference


* [ https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html ](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html)
* [ https://owasp.org/www-community/Security_Headers ](https://owasp.org/www-community/Security_Headers)
* [ https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security ](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security)
* [ https://caniuse.com/stricttransportsecurity ](https://caniuse.com/stricttransportsecurity)
* [ https://datatracker.ietf.org/doc/html/rfc6797 ](https://datatracker.ietf.org/doc/html/rfc6797)


#### CWE Id: [ 319 ](https://cwe.mitre.org/data/definitions/319.html)


#### WASC Id: 15

#### Source ID: 3

### [ X-Content-Type-Options Header Missing ](https://www.zaproxy.org/docs/alerts/10021/)



##### Low (Medium)

### Description

The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.

* URL: https://edge-consumer-static.azureedge.net/mouse-gesture/config.json
  * Node Name: `https://edge-consumer-static.azureedge.net/mouse-gesture/config.json`
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`
* URL: https://xpaywalletcdn-prod.azureedge.net/mswallet/ExpressCheckout/v1/GetGlobalConfig%3FEdgeChannel=stable&EdgeVersion=157.0.4341.57&ConfigVersion=0&ConfigType=DAF_CFG
  * Node Name: `https://xpaywalletcdn-prod.azureedge.net/mswallet/ExpressCheckout/v1/GetGlobalConfig (ConfigType,ConfigVersion,EdgeChannel,EdgeVersion)`
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`


Instances: 2

### Solution

Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.
If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.

### Reference


* [ https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/compatibility/gg622941(v=vs.85) ](https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/compatibility/gg622941(v=vs.85))
* [ https://owasp.org/www-community/Security_Headers ](https://owasp.org/www-community/Security_Headers)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 15

#### Source ID: 3

### [ Authentication Request Identified ](https://www.zaproxy.org/docs/alerts/10111/)



##### Informational (High)

### Description

The given request has been identified as an authentication request. The 'Other Info' field contains a set of key=value lines which identify any relevant fields. If the request is in a context which has an Authentication Method set to "Auto-Detect" then this rule will change the authentication to match the request identified.

* URL: http://127.0.0.1:8000/login/
  * Node Name: `http://127.0.0.1:8000/login/ ()(csrfmiddlewaretoken,password,username)`
  * Method: `POST`
  * Parameter: `username`
  * Attack: ``
  * Evidence: `password`
  * Other Info: `userParam=username
userValue=jefa
passwordParam=password
referer=http://127.0.0.1:8000/login/
csrfToken=csrfmiddlewaretoken`
* URL: http://127.0.0.1:8000/login/%3Fnext=/producto/2/
  * Node Name: `http://127.0.0.1:8000/login/ (next)(csrfmiddlewaretoken,password,username)`
  * Method: `POST`
  * Parameter: `username`
  * Attack: ``
  * Evidence: `password`
  * Other Info: `userParam=username
userValue=ana
passwordParam=password
referer=http://127.0.0.1:8000/login/?next=/producto/2/
csrfToken=csrfmiddlewaretoken`


Instances: 2

### Solution

This is an informational alert rather than a vulnerability and so there is nothing to fix.

### Reference


* [ https://www.zaproxy.org/docs/desktop/addons/authentication-helper/auth-req-id/ ](https://www.zaproxy.org/docs/desktop/addons/authentication-helper/auth-req-id/)



#### Source ID: 3

### [ Re-examine Cache-control Directives ](https://www.zaproxy.org/docs/alerts/10015/)



##### Informational (Low)

### Description

The cache-control header has not been set properly or is missing, allowing the browser and proxies to cache content. For static assets like css, js, or image files this might be intended, however, the resources should be reviewed to ensure that no sensitive content will be cached.

* URL: https://edge-consumer-static.azureedge.net/mouse-gesture/config.json
  * Node Name: `https://edge-consumer-static.azureedge.net/mouse-gesture/config.json`
  * Method: `GET`
  * Parameter: `cache-control`
  * Attack: ``
  * Evidence: `public, max-age=432000`
  * Other Info: ``
* URL: https://xpaywalletcdn-prod.azureedge.net/mswallet/ExpressCheckout/v1/GetGlobalConfig%3FEdgeChannel=stable&EdgeVersion=157.0.4341.57&ConfigVersion=0&ConfigType=DAF_CFG
  * Node Name: `https://xpaywalletcdn-prod.azureedge.net/mswallet/ExpressCheckout/v1/GetGlobalConfig (ConfigType,ConfigVersion,EdgeChannel,EdgeVersion)`
  * Method: `GET`
  * Parameter: `cache-control`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``


Instances: 2

### Solution

For secure content, ensure the cache-control HTTP header is set with "no-cache, no-store, must-revalidate". If an asset should be cached consider setting the directives "public, max-age, immutable".

### Reference


* [ https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html#web-content-caching ](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html#web-content-caching)
* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control)
* [ https://grayduck.mn/2021/09/13/cache-control-recommendations/ ](https://grayduck.mn/2021/09/13/cache-control-recommendations/)


#### CWE Id: [ 525 ](https://cwe.mitre.org/data/definitions/525.html)


#### WASC Id: 13

#### Source ID: 3

### [ Session Management Response Identified ](https://www.zaproxy.org/docs/alerts/10112/)



##### Informational (Medium)

### Description

The given response has been identified as containing a session management token. The 'Other Info' field contains a set of header tokens that can be used in the Header Based Session Management Method. If the request is in a context which has a Session Management Method set to "Auto-Detect" then this rule will change the session management to use the tokens identified.

* URL: http://127.0.0.1:8000/
  * Node Name: `http://127.0.0.1:8000/`
  * Method: `GET`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `csrftoken`
  * Other Info: `cookie:csrftoken`
* URL: http://127.0.0.1:8000/login/
  * Node Name: `http://127.0.0.1:8000/login/`
  * Method: `GET`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `csrftoken`
  * Other Info: `cookie:csrftoken`
* URL: http://127.0.0.1:8000/login/%3Fnext=/
  * Node Name: `http://127.0.0.1:8000/login/ (next)`
  * Method: `GET`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `csrftoken`
  * Other Info: `cookie:csrftoken`
* URL: http://127.0.0.1:8000/producto/3/editar/
  * Node Name: `http://127.0.0.1:8000/producto/3/editar/`
  * Method: `GET`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `csrftoken`
  * Other Info: `cookie:csrftoken`
* URL: http://127.0.0.1:8000/producto/3/eliminar/
  * Node Name: `http://127.0.0.1:8000/producto/3/eliminar/`
  * Method: `GET`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `csrftoken`
  * Other Info: `cookie:csrftoken`
* URL: http://127.0.0.1:8000/producto/4/editar/
  * Node Name: `http://127.0.0.1:8000/producto/4/editar/`
  * Method: `GET`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `csrftoken`
  * Other Info: `cookie:csrftoken`
* URL: http://127.0.0.1:8000/producto/4/eliminar/
  * Node Name: `http://127.0.0.1:8000/producto/4/eliminar/`
  * Method: `GET`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `csrftoken`
  * Other Info: `cookie:csrftoken`
* URL: http://127.0.0.1:8000/producto/nuevo/
  * Node Name: `http://127.0.0.1:8000/producto/nuevo/`
  * Method: `GET`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `csrftoken`
  * Other Info: `cookie:csrftoken`
* URL: http://127.0.0.1:8000/login/
  * Node Name: `http://127.0.0.1:8000/login/ ()(csrfmiddlewaretoken,password,username)`
  * Method: `POST`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `csrftoken`
  * Other Info: `cookie:csrftoken
cookie:sessionid`
* URL: http://127.0.0.1:8000/login/%3Fnext=/producto/2/
  * Node Name: `http://127.0.0.1:8000/login/ (next)(csrfmiddlewaretoken,password,username)`
  * Method: `POST`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `csrftoken`
  * Other Info: `cookie:csrftoken`
* URL: http://127.0.0.1:8000/producto/nuevo/
  * Node Name: `http://127.0.0.1:8000/producto/nuevo/ ()(csrfmiddlewaretoken,descripcion,nombre,precio,stock)`
  * Method: `POST`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `csrftoken`
  * Other Info: `cookie:csrftoken`
* URL: http://127.0.0.1:8000/login/
  * Node Name: `http://127.0.0.1:8000/login/ ()(csrfmiddlewaretoken,password,username)`
  * Method: `POST`
  * Parameter: `sessionid`
  * Attack: ``
  * Evidence: `sessionid`
  * Other Info: `cookie:sessionid`
* URL: http://127.0.0.1:8000/login/%3Fnext=/producto/2/
  * Node Name: `http://127.0.0.1:8000/login/ (next)(csrfmiddlewaretoken,password,username)`
  * Method: `POST`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `csrftoken`
  * Other Info: `cookie:csrftoken`
* URL: http://127.0.0.1:8000/login/%3Fnext=/producto/2/
  * Node Name: `http://127.0.0.1:8000/login/ (next)(csrfmiddlewaretoken,password,username)`
  * Method: `POST`
  * Parameter: `sessionid`
  * Attack: ``
  * Evidence: `sessionid`
  * Other Info: `cookie:sessionid`


Instances: 14

### Solution

This is an informational alert rather than a vulnerability and so there is nothing to fix.

### Reference


* [ https://www.zaproxy.org/docs/desktop/addons/authentication-helper/session-mgmt-id/ ](https://www.zaproxy.org/docs/desktop/addons/authentication-helper/session-mgmt-id/)



#### Source ID: 3

### [ User Controllable HTML Element Attribute (Potential XSS) ](https://www.zaproxy.org/docs/alerts/10031/)



##### Informational (Low)

### Description

This check looks at user-supplied input in query string parameters and POST data to identify where certain HTML attribute values might be controlled. This provides hot-spot detection for XSS (cross-site scripting) that will require further review by a security analyst to determine exploitability.

* URL: http://127.0.0.1:8000/login/%3Fnext=/producto/2/
  * Node Name: `http://127.0.0.1:8000/login/ (next)(csrfmiddlewaretoken,password,username)`
  * Method: `POST`
  * Parameter: `username`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled HTML attribute values were found. Try injecting special characters to see if XSS might be possible. The page at the following URL:

http://127.0.0.1:8000/login/?next=/producto/2/

appears to include user input in:
a(n) [input] tag [value] attribute

The user input found was:
username=ana

The user-controlled value was:
ana`
* URL: http://127.0.0.1:8000/producto/nuevo/
  * Node Name: `http://127.0.0.1:8000/producto/nuevo/ ()(csrfmiddlewaretoken,descripcion,nombre,precio,stock)`
  * Method: `POST`
  * Parameter: `nombre`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled HTML attribute values were found. Try injecting special characters to see if XSS might be possible. The page at the following URL:

http://127.0.0.1:8000/producto/nuevo/

appears to include user input in:
a(n) [input] tag [value] attribute

The user input found was:
nombre=comida perro

The user-controlled value was:
comida perro`
* URL: http://127.0.0.1:8000/producto/nuevo/
  * Node Name: `http://127.0.0.1:8000/producto/nuevo/ ()(csrfmiddlewaretoken,descripcion,nombre,precio,stock)`
  * Method: `POST`
  * Parameter: `precio`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled HTML attribute values were found. Try injecting special characters to see if XSS might be possible. The page at the following URL:

http://127.0.0.1:8000/producto/nuevo/

appears to include user input in:
a(n) [input] tag [value] attribute

The user input found was:
precio=-1

The user-controlled value was:
-1`
* URL: http://127.0.0.1:8000/producto/nuevo/
  * Node Name: `http://127.0.0.1:8000/producto/nuevo/ ()(csrfmiddlewaretoken,descripcion,nombre,precio,stock)`
  * Method: `POST`
  * Parameter: `stock`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled HTML attribute values were found. Try injecting special characters to see if XSS might be possible. The page at the following URL:

http://127.0.0.1:8000/producto/nuevo/

appears to include user input in:
a(n) [input] tag [value] attribute

The user input found was:
stock=20

The user-controlled value was:
20`


Instances: 4

### Solution

Validate all input and sanitize output it before writing to any HTML attributes.

### Reference


* [ https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html ](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)


#### CWE Id: [ 20 ](https://cwe.mitre.org/data/definitions/20.html)


#### WASC Id: 20

#### Source ID: 3


