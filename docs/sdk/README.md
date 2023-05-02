# SDK

## Overview

Optional multiline or single-line description in [CommonMark](http://commonmark.org/help/) or HTML.

### Available Operations

* [get_users](#get_users) - Returns a list of users.

## get_users

Optional extended description in CommonMark or HTML.

### Example Usage

```python
import sdk


s = sdk.SDK()


res = s.sdk.get_users()

if res.get_users_200_application_json_strings is not None:
    # handle response
```
