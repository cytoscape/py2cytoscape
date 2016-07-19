# -*- coding: utf-8 -*-

def check_response(res):
    """ Check HTTP response and raise exception if response is not OK. """
    try:
        res.raise_for_status() # Alternative is res.ok
    except Exception as exc:
        # Bad response code, e.g. if adding an edge with nodes that doesn't exist
        try:
            err_info = res.json()
            err_msg = err_info['message'] # or 'localizeMessage'
        except ValueError:
            err_msg = res.text[:40] # Take the first 40 chars of the response
        except KeyError:
            err_msg = res.text[:40] + ("(No 'message' in err_info dict: %s"
                                       % list(err_info.keys()))
        exc.args += (err_msg,)
        raise exc



