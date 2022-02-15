function removeElementAnimate(element, className) {
    element.classList.add('animate__animated')
    element.classList.add(className)
    setTimeout(() => {
        element.remove()
    }, 500)
}

try {
    const idInput = document.querySelector('.id-field')
    idInput.addEventListener('submit', function (e) {
        e.preventDefault()

        let currentUrl = document.URL
        axios.get(`${currentUrl}get/`, {
            params: {
                'user-id': document.querySelector('#access').value
            }
        })
            .then((response) => {
                if (response.data.name) {
                    let errorMessage = document.querySelector('.error')
                    if (errorMessage) {
                        removeElementAnimate(errorMessage, 'animate__fadeOutDown')
                    }

                    let userData = response.data
                    let node = document.querySelector('.stats')
                    let cloneStats = node.cloneNode(true);
                    node.remove()

                    setTimeout(() => {
                        let recommendationsDiv = cloneStats.childNodes[5]
                        let statsHelloText = cloneStats.childNodes[1]
                        let statsDivParent = cloneStats.childNodes[3]
                        let progressConversion = statsDivParent.childNodes[1].childNodes[3]
                        let textProgress = recommendationsDiv.childNodes[1]
                        let progressLtv = statsDivParent.childNodes[3].childNodes[3]

                        statsHelloText.innerHTML = `Привет, ${userData.name}`
                        textProgress.innerText = `Для достижения 75% конверсии необходимо провести ${userData.reminder} вводных, после которых купят абонемент`

                        progressConversion.style.setProperty('--value', userData.conversion)
                        progressLtv.style.setProperty('--value', userData.ltv)

                        progressConversion.setAttribute('aria-valuenow', userData.conversion)
                        progressLtv.setAttribute('aria-valuenow', userData.ltv)

                        cloneStats.classList.remove('hidden')
                        console.log(cloneStats)
                        document.querySelector('.container').appendChild(cloneStats)
                    }, 300)
                } else {
                    let errorData = response.data
                    if (!document.querySelector('.error-container')) {
                        let errorMessage = document.createElement('p')
                        let errorContainer = document.createElement('div')
                        errorContainer.classList.add('error-container')
                        errorMessage.innerText = errorData.error
                        errorMessage.classList.add('error')
                        errorContainer.classList.add('animate__animated')
                        errorContainer.classList.add('animate__bounceInLeft')
                        errorContainer.appendChild(errorMessage)
                        document.querySelector('.container').appendChild(errorContainer)
                        setTimeout(() => {
                            removeElementAnimate(errorContainer, 'animate__bounceOutLeft')
                        }, 3000)
                    }

                }
            });
    })
} catch {
    console.log('error')
}
