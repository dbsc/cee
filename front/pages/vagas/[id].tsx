import { GetServerSideProps } from 'next'
import { getSession } from 'next-auth/client'
import Head from 'next/head'
import { useRouter } from 'next/router'
import { DashBoardHeader } from '../../components/DashboardHeader'
import styles from '../../styles/vaga.module.scss'
import { FaCalendarAlt, FaMapMarkerAlt, FaRegMoneyBillAlt } from 'react-icons/fa'
import { StandartButton } from '../../components/StandartButton'
import axios from 'axios'

interface VagaProps {
	id: number
	title: string
	company: string
	field: string
	position: string
	pay: string
	date: string
	location: { city: string; state: string }
	description: string
	requirements: string[]
	responsibilities: string[]
	link: string
}

export default function Vaga(props: VagaProps) {
	const location = props.location ? `${props.location.state} - ${props.location.city}` : 'Remoto'
	const date = `Até ${props.date}` && 'Sem data'
	return (
		<>
			<Head>
				<title>Vaga | CEE</title>
			</Head>
			<DashBoardHeader />
			<div className={styles.container}>
				<div className={styles.content}>
					<div className={styles.box}>
						<div className={styles.mainInfo}>
							<div className={styles.title}>{props.title}</div>
							<div className={styles.subtitle}>{props.company}</div>

							<div className={styles.info1}>
								<div>Área: {props.field}</div>
								<div>Posição: {props.position}</div>
							</div>

							<div className={styles.icons}>
								<div className={styles.icon}>
									<FaMapMarkerAlt />
									<div>{location}</div>
								</div>
								<div className={styles.icon} id={styles.money}>
									<FaRegMoneyBillAlt />
									<div>{props.pay}</div>
								</div>
								<div className={styles.icon} id={styles.data}>
									<FaCalendarAlt />
									<div>
										<span>{date}</span>
									</div>
								</div>
							</div>

							<StandartButton link={props.link}>Candidar-se</StandartButton>

							{/* <div>Essa é a vaga de id: {props.id}</div> */}
						</div>

						<div className={styles.description}>
							<div className={styles.title}>DESCRIÇÃO DA VAGA</div>
							<div>{props.description}</div>
							<div className={styles.subtitle}>Responsabilidades</div>
							{props.responsibilities.map((elem, index) => (
								<div key={index}>
									{elem} <br />
								</div>
							))}

							<div className={styles.subtitle}>Requisitos</div>
							{props.requirements.map((elem, index) => (
								<div key={index}>
									{elem} <br />
								</div>
							))}
						</div>
					</div>

					<div className={styles.button}>
						<StandartButton link={props.link}>CANDIDATAR-SE</StandartButton>
					</div>
				</div>
			</div>
		</>
	)
}

export const getServerSideProps: GetServerSideProps = async ({ req, params }) => {
	const session = await getSession({ req })
	const { id } = params

	// axios
	// 	.get(`https//localhost:8000/vacancies/vacancies/${id}`)
	// 	.then((response) => {
	// 		const vaga: Vaga = {
	// 			id: response.data.id,
	// 			title: response.data.title,
	// 			company: response.data.company,
	// 			field: response.data.field,
	// 			position: response.data.position,
	// 			pay: new Intl.NumberFormat('pr-BR', { style: 'currency', currency: 'BRL' }).format(
	// 				response.data
	// 			),
	// 			date: response.data.expiration_date,
	// 		}
	// 	})
	// 	.catch((err) => {
	// 		console.error('Ocorreu um erro' + err)
	// 	})

	const response = await axios.get(`http://127.0.0.1:8000/vacancies/vacancies/${id}`)

	const vaga: VagaProps = {
		id: response.data.id,
		title: response.data.title,
		company: response.data.company.name,
		field: response.data.field,
		position: response.data.position,
		pay: new Intl.NumberFormat('pr-BR', { style: 'currency', currency: 'BRL' }).format(
			response.data.pay
		),
		date: response.data.expiration_date,
		description: response.data.description,
		location: response.data.location,
		requirements: response.data.requirements.preferred,
		responsibilities: response.data.responsibilities,
		link: response.data.link,
	}
	// console.log(response.data)
	console.log(vaga)

	if (!session) {
		return {
			redirect: {
				destination: '/',
				permanent: false,
			},
		}
	}

	return {
		props: vaga,
	}
}
