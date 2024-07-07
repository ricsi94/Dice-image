import * as THREE from "three"
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls.js"
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader.js"
import pythonOutput from "./output.json"

const renderer = new THREE.WebGLRenderer()
renderer.setSize(window.innerWidth, window.innerHeight)
document.body.appendChild(renderer.domElement)
const scene = new THREE.Scene()

// Add camera
const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000)
camera.position.set(100, 200, 100)
const lookAtPoint = new THREE.Vector3(100, 0, 100)
camera.lookAt(lookAtPoint)
// TODO: orbit control - kamera rotációt megoldani
//camera.rotateOnAxis(new THREE.Vector3(0, 0, 1), -Math.PI / 2);

// Add orbit control
const orbit = new OrbitControls(camera, renderer.domElement)
orbit.target = lookAtPoint // Set the target of the OrbitControls
orbit.update()

// Add light
const ambientLight = new THREE.AmbientLight(0xffffff, 0.9)

scene.add(ambientLight)

// Load dice model
const assetLoader = new GLTFLoader()
let model = null
assetLoader.load(
	"./dice.gltf",
	function (gltf) {
		model = gltf.scene
	},
	undefined,
	(error) => {
		console.error(error)
	}
)

// First object
const modelPosition = new THREE.Vector3(8, 2, 0)

let objects = []
let positions = []
positions.push(modelPosition)
let alreadyAdded = false

function animate() {
	if (model && !alreadyAdded) {
		// TODO: Kiszedni innen a kamera rotációt
		camera.rotateOnAxis(new THREE.Vector3(0, 0, 1), -Math.PI * 0.15)

		for (let i = 0; i < pythonOutput.length; i++) {
			let xCoord = pythonOutput[i].xCoord
			let yCoord = pythonOutput[i].yCoord
			let numberOnTopOfDice = pythonOutput[i].numberOnTopOfDice

			let dice = model.clone()
			dice.position.set(xCoord * 2, 2, yCoord * 2)

			switch (numberOnTopOfDice) {
				case "1":
					dice.rotateX(Math.PI / 2)
					break
				case "2":
					dice.rotateX(Math.PI)
					break
				case "3":
					dice.rotateX(-Math.PI / 2)
					break
				case "5":
					dice.rotateZ(-Math.PI / 2)
					break
				case "6":
					dice.rotateZ(Math.PI / 2)
					break
			}

			objects.push(dice)
			scene.add(dice)
		}
		alreadyAdded = true
	}

	renderer.render(scene, camera)
	requestAnimationFrame(animate)
}
animate()

window.addEventListener("resize", function () {
	camera.aspect = window.innerWidth / window.innerHeight
	camera.updateProjectionMatrix()
	renderer.setSize(window.innerWidth, window.innerHeight)
})
