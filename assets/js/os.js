// JavaScript to detect user's operating system
(function () {
    var os = navigator.platform.toLowerCase();
    var buttons = document.querySelectorAll('.button');

    for (var i = 0; i < buttons.length; i++) {
        var button = buttons[i];
        var osType = button.getAttribute('data-for-os');

        if (osType && os.indexOf(osType.toLowerCase()) === -1) {
            button.style.display = 'none';
        }
    }
})();