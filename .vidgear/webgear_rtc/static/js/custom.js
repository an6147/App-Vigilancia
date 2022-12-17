// intialize
var pc = null;
// define negotiate function
function negotiate() {
    //  creates a new RTCRtpTransceiver `video` and adds it to the 
    //set of transceivers associated with the RTCPeerConnection
    pc.addTransceiver('video', {
        direction: 'recvonly'
    });
    // create and return  SDP offer for the purpose 
    // of starting a new WebRTC connection to a remote peer
    return pc.createOffer().then(function(offer) {
        return pc.setLocalDescription(offer);
    }).then(function() {
        // wait for ICE gathering to complete
        return new Promise(function(resolve) {
            if (pc.iceGatheringState === 'complete') {
                resolve();
            } else {
                function checkState() {
                    if (pc.iceGatheringState === 'complete') {
                        // remove `icegatheringstatechange` event listener
                        pc.removeEventListener('icegatheringstatechange', checkState);
                        resolve();
                    }
                }
                // add `icegatheringstatechange` event listener
                pc.addEventListener('icegatheringstatechange', checkState);
            }
        });
    }).then(function() {
        // build and return json offer.
        var offer = pc.localDescription;
        return fetch('/offer', {
            body: JSON.stringify({
                sdp: offer.sdp,
                type: offer.type,
            }),
            headers: {
                'Content-Type': 'application/json'
            },
            method: 'POST'
        });
    }).then(function(response) {
        // return response
        return response.json();
    }).then(function(answer) {
        // return session description as the 
        // remote peer's current answer. 
        return pc.setRemoteDescription(answer);
    }).catch(function(e) {
        // catch any errors.
        alert(e);
    });
}
// add configs
var config = {
    sdpSemantics: 'unified-plan'
};
// add STUN protocol to discover your public address 
// and determine any restrictions in your router that 
// would prevent a direct connection with a peer.
config.iceServers = [{
    urls: ['stun:stun.l.google.com:19302']
}];
// create new RTCPeerConnection, which represents 
// a connection between the local device and a remote peer.
pc = new RTCPeerConnection(config);
// connect to video and assign to video element source. 
pc.addEventListener('track', function(evt) {
    if (evt.track.kind == 'video') {
        document.getElementById('video').srcObject = evt.streams[0];
    }
});
// call negotiate
negotiate();

// Call 'close_connection' endpoint to inform server that we are refreshing page
window.onbeforeunload = function(event) {
    pc.close();
    pc = null;
    axios.post('/close_connection', 1); // POST
};