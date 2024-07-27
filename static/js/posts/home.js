
const postBox =  document.getElementById("post-box")
const spinnerBox = document.getElementById("spinner-box")
const loadBtn = document.getElementById("load-btn")
const endBox = document.getElementById("end-box")


let visible = 3

const getData = () => {
    $.ajax({
        type: "GET",
        url: `/data/${visible}/`,
        success: function(response){
            // console.log(response)
            const data = response.data
            setTimeout(() => {
                spinnerBox.classList.add("not-visible")
                data.forEach(el => {
                    const truncateWords = (text, wordLimit) => {
                        const words = text.split(" ")
                        return words.length > wordLimit ? words.slice(0, wordLimit).join(" ") + "..." : text
                    }
                    postBox.innerHTML += `
                        <div class="card my-4 h-100 shadow border-light">
                            <div class="card-body">
                                <h5 class="card-title">${truncateWords(el.title, 10)}</h5>
                                <hr>
                                <p class="card-text">${truncateWords(el.body, 50)}</p>
                                </div>
                                <div class="card-footer">
                                <div class="row">
                                    <div class="col-1">
                                        <a href="#" class="btn btn-primary">Details</a>
                                    </div>
                                    <div class="col-1">
                                        <a href="#" class="btn btn-primary">Like</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    `
                });
            }, 100)
            console.log(response.size)
            if (response.size === 0) {
                endBox.textContent = "No posts added yet..."
            } else if (response.size <= visible){
                loadBtn.classList.add("not-visible")
                endBox.textContent = "No more posts to load..."
            }
        },
        error: function(error){
            console.log(error)
        }
    })
}

loadBtn.addEventListener("click", () => {
    spinnerBox.classList.remove("not-visible")
    visible += 3
    getData()
})

getData()