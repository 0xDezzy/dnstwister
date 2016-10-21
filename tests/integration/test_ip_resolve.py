"""Test respolving IPs."""
import socket


def test_resolve(webapp):
    """Test we can resolve IP addresses."""
    response = webapp.get('/api/ip/646e73747769737465722e7265706f7274')

    assert response.status_code == 200

    payload = response.json
    ip = payload['ip']
    del payload['ip']

    assert payload == {
        u'domain': u'dnstwister.report',
        u'domain_as_hexadecimal': u'646e73747769737465722e7265706f7274',
        u'error': False,
        u'fuzz_url': u'http://localhost:80/api/fuzz/646e73747769737465722e7265706f7274',
        u'parked_score_url': u'http://localhost:80/api/parked/646e73747769737465722e7265706f7274',
        u'url': u'http://localhost:80/api/ip/646e73747769737465722e7265706f7274'
    }

    # Will throw if invalid IP
    socket.inet_aton(ip)