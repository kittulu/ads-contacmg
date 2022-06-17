package com.unesc.myfinances.dto;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.List;
import java.util.stream.Collectors;

import com.unesc.myfinances.entities.Finances;
import com.unesc.myfinances.entities.FinancesTipo;
import com.unesc.myfinances.entities.Situacao;
import com.unesc.myfinances.entities.Usuario;

import lombok.Data;

@Data
public class FinancesGetResponseDTO {

	private String descricao;
	private Usuario usuario;
	private Situacao situacao;
	private FinancesTipo financesTipo;
	private Integer parcela;
	private Integer totalParcela;
	private BigDecimal valorParcela;
	private BigDecimal valorTotal;
	private LocalDate dataVencimento;
	
	public static FinancesGetResponseDTO convert(Finances finances) {
		FinancesGetResponseDTO finDTO = new FinancesGetResponseDTO();
		finDTO.setDescricao(finances.getDescricao());
		finDTO.setUsuario(finances.getUsuario());
		finDTO.setSituacao(finances.getSituacao());
		finDTO.setFinancesTipo(finances.getFinancesTipo());
		finDTO.setParcela(finances.getParcela());
		finDTO.setTotalParcela(finances.getTotalParcela());
		finDTO.setValorParcela(finances.getValorParcela());
		finDTO.setValorTotal(finances.getValorTotal());
		finDTO.setDataVencimento(finances.getDataVencimento());
		
		return finDTO;
	}
	
	public static List<FinancesGetResponseDTO> convertList(List<Finances> finList){
		return finList.stream().map(FinancesGetResponseDTO::convert).collect(Collectors.toList());
	}
}
