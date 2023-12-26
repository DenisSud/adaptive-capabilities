package main

import (
	"fmt"
	"image"
	"sync"

	"github.com/zergon321/reisen"
)


func main() {
	// var diametters []float64 // slice of diamiters 
	// var wg sync.WaitGroup // wait group(concurency)

	// Open the video file.
	media, err := reisen.NewMedia("test.mp4")
	handleError(err)
	fmt.Print(media)
    // // Loop over all the frames of the video.
    // for {
    //     // Read the next frame from the decoder.
    //     var frame image.Image
	// 	wg.Add(1)
	// 	go findDiametter(diametters, frame, &wg) // run a go routine to find the diametter
	// }

    // // Wait for all the concurrent goroutines to finish.
    // wg.Wait()
}


// This function is declared outside of the main function.
func findDiametter(data []float64, frame image.Image, wg *sync.WaitGroup) {
	var D float64
	// finished
	data =
	append(data, D)
}


func handleError(err error) {
	if err != nil {
		panic(err)
	}
}
